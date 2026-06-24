# Импорты
from flask import Flask, render_template, request, redirect, session, jsonify, g
import sqlite3
import smtplib
from email.mime.text import MIMEText
import os
import secrets
import time
import hashlib
from datetime import datetime
from dotenv import load_dotenv
import traceback
import logging
from logging.handlers import RotatingFileHandler
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Загружаем переменные окружения из .env файла
load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Секретный ключ для сессий

# Настройка логирования
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler(
    'logs/blog.log',
    maxBytes=10240,  # 10KB
    backupCount=10
)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Блог запущен')

# Rate Limiting
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Подключение к базе данных
conn = sqlite3.connect('users.db', check_same_thread=False)
cur = conn.cursor()

# Создание таблицы пользователей
cur.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT,
            last_login TIMESTAMP,
            role TEXT DEFAULT 'user'
)''')

# Создание таблицы категорий
cur.execute('''CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT
)''')

# Создание таблицы постов
cur.execute('''CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            user_id INTEGER,
            category_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
)''')

# Создание таблицы уведомлений
cur.execute('''CREATE TABLE IF NOT EXISTS notifications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action TEXT,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
)''')

# Создание таблицы токенов аутентификации
cur.execute('''CREATE TABLE IF NOT EXISTS auth_tokens(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            token TEXT UNIQUE,
            expires_at TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
)''')

default_categories = [
    ('Программирование', 'Статьи о программировании и разработке'),
    ('Дизайн', 'Статьи о дизайне и UX/UI'),
    ('Путешествия', 'Рассказы о путешествиях'),
    ('Кулинария', 'Рецепты и кулинарные советы'),
    ('Спорт', 'Новости и статьи о спорте')
]

for category in default_categories:
    cur.execute('INSERT OR IGNORE INTO categories(name, description) VALUES (?, ?)', category)

cur.execute("UPDATE users SET role = 'user' WHERE role IS NULL")
cur.execute('CREATE INDEX IF NOT EXISTS idx_user_id ON posts(user_id)')
cur.execute('CREATE INDEX IF NOT EXISTS idx_notif_user_id ON notifications(user_id)')
cur.execute('CREATE INDEX IF NOT EXISTS idx_token ON auth_tokens(token)')
cur.execute('CREATE INDEX IF NOT EXISTS idx_category_id ON posts(category_id)')
cur.execute('CREATE INDEX IF NOT EXISTS idx_post_title ON posts(title)')
cur.execute('CREATE INDEX IF NOT EXISTS idx_post_content ON posts(content)')

admin_email = 'Test@gmail.com'
cur.execute("SELECT * FROM users WHERE email = ?", [admin_email])
if not cur.fetchone():
    hashed_admin = generate_password_hash('admin123')
    cur.execute("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
                ['Администратор', admin_email, hashed_admin, 'admin'])
    conn.commit()
    app.logger.info('Создан администратор по умолчанию')

# Сохранение изменений в базе данных
conn.commit()

# Простой кэш в памяти
cache = {}

def get_cached_posts(page, per_page, category_id=None, sort_by='created_at', order='desc', search_query=None):
    cache_key = f'posts_{page}_{per_page}_{category_id}_{sort_by}_{order}_{search_query}'
    if cache_key in cache:
        cached_data, timestamp = cache[cache_key]
        if time.time() - timestamp < 60:
            return cached_data
    offset = (page - 1) * per_page
    query = '''
        SELECT posts.*, users.name, categories.name as category_name
        FROM posts 
        JOIN users ON posts.user_id = users.id
        LEFT JOIN categories ON posts.category_id = categories.id
    '''
    params = []
    conditions = []
    if category_id:
        conditions.append('posts.category_id = ?')
        params.append(category_id)
    if search_query:
        conditions.append('(posts.title LIKE ? OR posts.content LIKE ?)')
        search_pattern = f'%{search_query}%'
        params.extend([search_pattern, search_pattern])
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    if sort_by == 'title':
        order_by = 'posts.title'
    else:
        order_by = 'posts.created_at'
    query += f' ORDER BY {order_by} {order}'
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    cur.execute(query, params)
    posts = cur.fetchall()
    cache[cache_key] = (posts, time.time())
    return posts

# Функция отправки welcome-письма
def send_welcome_email(to_email, username):
    from_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")
    if not from_email or not password:
        app.logger.error('EMAIL_USER или EMAIL_PASSWORD не установлены')
        return False
    subject = "Добро пожаловать в наш блог!"
    body = f"""
    Привет, {username}!
    Спасибо за регистрацию в нашем блоге.
    С уважением,
    Команда блога
    """
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        app.logger.info(f'Письмо успешно отправлено на {to_email}')
        return True
    except smtplib.SMTPAuthenticationError:
        app.logger.error('Ошибка аутентификации при отправке письма')
    except Exception as e:
        app.logger.error(f'Ошибка отправки письма: {e}')
    return False

# Добавляет нового пользователя и возвращает его ID
def add_user(name, email, password):
    hashed_password = generate_password_hash(password)
    cur.execute('INSERT INTO users(name, email, password, last_login) VALUES (?, ?, ?, ?)',
                [name, email, hashed_password, datetime.now()])
    conn.commit()
    cur.execute('SELECT id FROM users WHERE email = ?', [email])
    return cur.fetchone()[0]

# Возвращает пользователя по его ID
def get_user_by_id(user_id):
    cur.execute('SELECT * FROM users WHERE id = ?', [user_id])
    return cur.fetchone()

# Возвращает пользователя по его электронной почте
def get_user_by_email(email):
    cur.execute('SELECT * FROM users WHERE email = ?', [email])
    return cur.fetchone()

# Обновляет время последнего входа
def update_last_login(user_id):
    cur.execute('UPDATE users SET last_login = ? WHERE id = ?',
                [datetime.now(), user_id])
    conn.commit()

# Добавляет новый пост с привязкой к пользователю
def add_new_post(title, content, user_id, category_id):
    cur.execute('INSERT INTO posts(title, content, user_id, category_id) VALUES (?, ?, ?, ?)',
                [title, content, user_id, category_id])
    conn.commit()
    global cache
    cache = {}

def get_all_categories():
    cur.execute('SELECT * FROM categories ORDER BY name')
    return cur.fetchall()

# Возвращает посты пользователя
def get_posts_by_user(user_id):
    cur.execute('SELECT * FROM posts WHERE user_id = ? ORDER BY created_at DESC', [user_id])
    return cur.fetchall()

def get_posts_by_category(category_id):
    cur.execute('''SELECT posts.*, users.name, categories.name as category_name
                   FROM posts 
                   JOIN users ON posts.user_id = users.id
                   LEFT JOIN categories ON posts.category_id = categories.id
                   WHERE posts.category_id = ? 
                   ORDER BY posts.created_at DESC''',
                [category_id])
    return cur.fetchall()

# Функция для поиска постов
def search_posts(query):
    search_pattern = f'%{query}%'
    cur.execute('''SELECT posts.*, users.name, categories.name as category_name
                   FROM posts 
                   JOIN users ON posts.user_id = users.id
                   LEFT JOIN categories ON posts.category_id = categories.id
                   WHERE posts.title LIKE ? OR posts.content LIKE ?
                   ORDER BY posts.created_at DESC''',
                [search_pattern, search_pattern])
    return cur.fetchall()

# Функция для получения всех пользователей
def get_all_users():
    cur.execute('SELECT * FROM users')
    return cur.fetchall()

# Создает токен аутентификации
def create_auth_token(user_id, remember=False):
    token = secrets.token_hex(32)
    if remember:
        expires_at = time.time() + 30 * 24 * 60 * 60  # 30 дней
    else:
        expires_at = time.time() + 60 * 60  # 1 час
    cur.execute('INSERT INTO auth_tokens(user_id, token, expires_at) VALUES (?, ?, ?)',
                [user_id, token, expires_at])
    conn.commit()
    return token

# Проверяет токен аутентификации
def validate_auth_token(token):
    cur.execute('SELECT user_id FROM auth_tokens WHERE token = ? AND expires_at > ?', [token, time.time()])
    result = cur.fetchone()
    if result:
        return result[0]
    return None

# Удаляет токен аутентификации
def delete_auth_token(token):
    cur.execute('DELETE FROM auth_tokens WHERE token = ?', [token])
    conn.commit()

# Логирует уведомление
def log_notification(user_id, action, details):
    cur.execute('INSERT INTO notifications(user_id, action, details) VALUES (?, ?, ?)',
                [user_id, action, details])
    conn.commit()

# Возвращает уведомления пользователя
def get_notifications_by_user(user_id):
    cur.execute('SELECT * FROM notifications WHERE user_id = ? ORDER BY created_at DESC',
                [user_id])
    return cur.fetchall()

def is_admin(user_id):
    if not user_id:
        return False
    cur.execute("SELECT role FROM users WHERE id = ?", [user_id])
    result = cur.fetchone()
    return result and result[0] == 'admin'

def get_current_user_role():
    user_id = session.get('user_id')
    if not user_id:
        return None
    cur.execute("SELECT role FROM users WHERE id = ?", [user_id])
    result = cur.fetchone()
    return result[0] if result else None

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_id'):
            app.logger.warning('Попытка доступа к админ-панели без авторизации')
            return redirect('/login/')
        if not is_admin(session.get('user_id')):
            app.logger.warning(f'Попытка несанкционированного доступа к админ-панели пользователем {session.get("user_id")}')
            return render_template('403.html'), 403
        return f(*args, **kwargs)
    return decorated_function

def update_post(post_id, title, content, category_id):
    cur.execute('''
        UPDATE posts 
        SET title = ?, content = ?, category_id = ?
        WHERE id = ?
    ''', [title, content, category_id, post_id])
    conn.commit()

def update_user(user_id, name=None, email=None, role=None):
    updates = []
    params = []
    if name:
        updates.append("name = ?")
        params.append(name)
    if email:
        updates.append("email = ?")
        params.append(email)
    if role:
        updates.append("role = ?")
        params.append(role)
    if not updates:
        return False
    params.append(user_id)
    query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
    cur.execute(query, params)
    conn.commit()
    return True

def get_extended_stats():
    stats = {}
    cur.execute("SELECT COUNT(*) FROM users")
    stats['user_count'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM posts")
    stats['post_count'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM categories")
    stats['category_count'] = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM notifications")
    stats['notification_count'] = cur.fetchone()[0]
    cur.execute('''
        SELECT DATE(created_at) as day, COUNT(*) as count
        FROM posts 
        WHERE created_at >= DATE('now', '-7 days')
        GROUP BY DATE(created_at)
        ORDER BY day DESC
    ''')
    stats['posts_by_day'] = cur.fetchall()
    cur.execute('''
        SELECT users.name, COUNT(posts.id) as post_count
        FROM users 
        LEFT JOIN posts ON users.id = posts.user_id
        WHERE posts.created_at >= DATE('now', '-30 days')
        GROUP BY users.id
        ORDER BY post_count DESC
        LIMIT 5
    ''')
    stats['active_users'] = cur.fetchall()
    cur.execute('''
        SELECT categories.name, COUNT(posts.id) as count
        FROM categories 
        LEFT JOIN posts ON categories.id = posts.category_id
        GROUP BY categories.id
        ORDER BY count DESC
    ''')
    stats['posts_by_category'] = cur.fetchall()
    cur.execute('''
        SELECT name, email, last_login
        FROM users 
        ORDER BY last_login DESC
        LIMIT 5
    ''')
    stats['recent_users'] = cur.fetchall()
    return stats

# Middleware для проверки аутентификации
@app.before_request
def check_auth():
    if 'user_id' not in session:
        token = request.cookies.get('auth_token')
        if token:
            user_id = validate_auth_token(token)
            if user_id:
                user = get_user_by_id(user_id)
                if user:
                    session['user_id'] = user[0]
                    session['user_name'] = user[1]

# Рендерим стартовую страницу с пагинацией
@app.route('/')
def main():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 5
        cur.execute('SELECT COUNT(*) FROM posts')
        total_posts = cur.fetchone()[0]
        posts = get_cached_posts(page, per_page)
        users = cur.execute('SELECT * FROM users').fetchall()
        user_name = None
        if 'user_id' in session:
            user_name = session['user_name']
        total_pages = (total_posts + per_page - 1) // per_page
        return render_template('main.html',
                             posts=posts,
                             users=users,
                             user_name=user_name,
                             current_page=page,
                             total_pages=total_pages,
                             per_page=per_page)
    except Exception as e:
        app.logger.error(f'Ошибка на главной странице: {e}')
        raise

# API для получения постов с пагинацией (JSON)
@app.route('/api/posts')
def api_posts():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)
        posts = get_cached_posts(page, per_page)
        posts_list = []
        for post in posts:
            posts_list.append({
                'id': post[0],
                'title': post[1],
                'content': post[2][:200] + '...' if len(post[2]) > 200 else post[2],
                'user_id': post[3],
                'category_id': post[4],
                'created_at': post[5],
                'author': post[6],
                'category': post[7] if post[7] else 'Без категории'
            })
        cur.execute('SELECT COUNT(*) FROM posts')
        total = cur.fetchone()[0]
        return jsonify({
            'posts': posts_list,
            'page': page,
            'per_page': per_page,
            'total': total,
            'total_pages': (total + per_page - 1) // per_page
        })
    except Exception as e:
        app.logger.error(f'Ошибка в API постов: {e}')
        return jsonify({'error': 'Внутренняя ошибка сервера'}), 500

# Регистрация пользователя
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        app.logger.info(f'Попытка регистрации: {email}')
        user = get_user_by_email(email)
        if user is None:
            try:
                user_id = add_user(name, email, password)
                app.logger.info(f'Пользователь зарегистрирован: {email} (ID: {user_id})')
                email_sent = send_welcome_email(email, name)
                if email_sent:
                    log_notification(user_id, 'welcome_email_sent',
                                   f'Приветственное письмо отправлено на {email}')
                else:
                    log_notification(user_id, 'welcome_email_failed',
                                   f'Не удалось отправить письмо на {email}')
                return redirect('/login/')
            except Exception as e:
                app.logger.error(f'Ошибка при регистрации: {e}')
                return render_template('register.html',
                                     error='Ошибка при регистрации. Попробуйте позже.')
        else:
            app.logger.warning(f'Попытка повторной регистрации: {email}')
            return render_template('register.html',
                                 error='Пользователь с таким email уже существует.')
    return render_template('register.html')

# Процесс входа
@app.route('/login/', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember')
        user = get_user_by_email(email)
        if user is None:
            app.logger.warning(f'Попытка входа с несуществующим email: {email}')
            return render_template('login.html', message="Нет такой почты")
        if check_password_hash(user[3], password):
            app.logger.info(f'Вход выполнен: {email}')
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            update_last_login(user[0])
            if remember:
                token = create_auth_token(user[0], remember=True)
                response = redirect(f'/user/{user[0]}')
                response.set_cookie('auth_token', token, max_age=30*24*60*60)
            else:
                response = redirect(f'/user/{user[0]}')
            log_notification(user[0], 'login', 'Пользователь вошел в систему')
            return response
        else:
            app.logger.warning(f'Неверный пароль для: {email}')
            return render_template('login.html', message="Пароль неверный")
    return render_template('login.html')

# Выход из системы
@app.route('/logout')
def logout():
    token = request.cookies.get('auth_token')
    if token:
        delete_auth_token(token)
    user_id = session.get('user_id')
    if user_id:
        log_notification(user_id, 'logout', 'Пользователь вышел из системы')
    session.clear()
    response = redirect('/')
    response.set_cookie('auth_token', '', expires=0)
    return response

# Страница пользователя
@app.route('/user/<int:user_id>')
def user_page(user_id):
    try:
        user = get_user_by_id(user_id)
        if not user:
            app.logger.warning(f'Попытка доступа к несуществующему пользователю: {user_id}')
            return render_template('404.html'), 404
        posts = get_posts_by_user(user_id)
        notifications = get_notifications_by_user(user_id)
        return render_template('user_page.html', user=user, posts=posts, notifications=notifications)
    except Exception as e:
        app.logger.error(f'Ошибка на странице пользователя {user_id}: {e}')
        return render_template('500.html'), 500

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category_id = request.form.get('category')
        if 'user_id' in session:
            user_id = session['user_id']
        else:
            return redirect('/login/')
        try:
            add_new_post(title, content, user_id, category_id)
            cur.execute('SELECT name FROM categories WHERE id = ?', [category_id])
            category_name = cur.fetchone()
            category_name = category_name[0] if category_name else 'Неизвестно'
            log_notification(user_id, 'new_post',
                            f'Создан пост "{title}" в категории "{category_name}"')
            app.logger.info(f'Создан новый пост: {title} пользователем {user_id}')
            return redirect('/')
        except Exception as e:
            app.logger.error(f'Ошибка при создании поста: {e}')
            return render_template('new_post.html',
                                 categories=get_all_categories(),
                                 error='Ошибка при создании поста. Попробуйте позже.')
    categories = get_all_categories()
    return render_template('new_post.html', categories=categories)

# Маршрут для поиска
@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        try:
            posts = search_posts(query)
            app.logger.info(f'Выполнен поиск: {query}')
            return render_template('main.html',
                                 posts=posts,
                                 users=get_all_users(),
                                 user_name=session.get('user_name'),
                                 search_query=query)
        except Exception as e:
            app.logger.error(f'Ошибка при поиске: {e}')
            return render_template('main.html',
                                 posts=[],
                                 users=get_all_users(),
                                 user_name=session.get('user_name'),
                                 search_query=query,
                                 error='Ошибка при поиске')
    return redirect('/')

# Маршрут для отображения постов по категории
@app.route('/category/<int:category_id>')
def category_posts(category_id):
    try:
        posts = get_posts_by_category(category_id)
        cur.execute('SELECT * FROM categories WHERE id = ?', [category_id])
        category = cur.fetchone()
        if not category:
            app.logger.warning(f'Категория не найдена: {category_id}')
            return render_template('404.html'), 404
        return render_template('category.html',
                             posts=posts,
                             category=category,
                             user_name=session.get('user_name'))
    except Exception as e:
        app.logger.error(f'Ошибка при загрузке категории {category_id}: {e}')
        return render_template('500.html'), 500

# Тестовый маршрут для генерации 500 ошибки
@app.route('/test_500')
def test_500():
    raise Exception("Это тестовая ошибка 500!")

# Тестовый маршрут для дебага
@app.route('/debug_test')
def debug_test():
    result = 10 / 0
    return str(result)

# Обработка ошибки 404
@app.errorhandler(404)
def page_not_found(e):
    app.logger.error(f'404 ошибка: {e}')
    return render_template('404.html'), 404

# Обработка ошибки 500
@app.errorhandler(500)
def internal_server_error(e):
    app.logger.error(f'500 ошибка: {e}')
    return render_template('500.html'), 500

@app.errorhandler(403)
def forbidden_error(e):
    app.logger.error(f'403 ошибка: {e}')
    return render_template('403.html'), 403

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({"success": False, "error": "Слишком много запросов. Попробуйте позже."}), 429

# Обработка всех исключений
@app.errorhandler(Exception)
def handle_all_errors(e):
    if app.debug:
        error_traceback = traceback.format_exc()
        return render_template('debug_error.html',
                             error_type=type(e).__name__,
                             error_message=str(e),
                             error_traceback=error_traceback), 500
    else:
        app.logger.error(f'Необработанная ошибка: {e}\n{traceback.format_exc()}')
        return render_template('500.html'), 500


@app.route('/admin/')
@admin_required
def admin_dashboard():
    try:
        stats = get_extended_stats()
        cur.execute('''
            SELECT notifications.*, users.name 
            FROM notifications 
            JOIN users ON notifications.user_id = users.id 
            ORDER BY created_at DESC 
            LIMIT 5
        ''')
        recent_actions = cur.fetchall()
        app.logger.info(f'Админ-панель открыта пользователем {session.get("user_id")}')
        return render_template('admin_dashboard.html',
                             stats=stats,
                             recent_actions=recent_actions,
                             user_name=session.get('user_name'))
    except Exception as e:
        app.logger.error(f'Ошибка в админ-панели: {e}')
        return render_template('500.html'), 500

@app.route('/admin/users')
@admin_required
def admin_users():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 10
        offset = (page - 1) * per_page
        cur.execute('''
            SELECT id, name, email, role, last_login 
            FROM users 
            ORDER BY id DESC 
            LIMIT ? OFFSET ?
        ''', [per_page, offset])
        users = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM users")
        total_users = cur.fetchone()[0]
        total_pages = (total_users + per_page - 1) // per_page
        return render_template('admin_users.html',
                             users=users,
                             current_page=page,
                             total_pages=total_pages,
                             user_name=session.get('user_name'))
    except Exception as e:
        app.logger.error(f'Ошибка в управлении пользователями: {e}')
        return render_template('500.html'), 500

@app.route('/admin/posts')
@admin_required
def admin_posts():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 10
        offset = (page - 1) * per_page
        cur.execute('''
            SELECT posts.*, users.name as author_name, categories.name as category_name
            FROM posts 
            LEFT JOIN users ON posts.user_id = users.id
            LEFT JOIN categories ON posts.category_id = categories.id
            ORDER BY posts.created_at DESC 
            LIMIT ? OFFSET ?
        ''', [per_page, offset])
        posts = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM posts")
        total_posts = cur.fetchone()[0]
        total_pages = (total_posts + per_page - 1) // per_page
        return render_template('admin_posts.html',
                             posts=posts,
                             current_page=page,
                             total_pages=total_pages,
                             user_name=session.get('user_name'))
    except Exception as e:
        app.logger.error(f'Ошибка в управлении постами: {e}')
        return render_template('500.html'), 500

@app.route('/admin/post/delete/<int:post_id>')
@admin_required
def admin_delete_post(post_id):
    try:
        cur.execute("SELECT title, user_id FROM posts WHERE id = ?", [post_id])
        post = cur.fetchone()
        if not post:
            app.logger.warning(f'Попытка удаления несуществующего поста {post_id}')
            return render_template('404.html'), 404
        cur.execute("DELETE FROM posts WHERE id = ?", [post_id])
        conn.commit()
        log_notification(session['user_id'], 'admin_post_delete',
                        f'Администратор удалил пост "{post[0]}" (ID: {post_id}) автора {post[1]}')
        app.logger.info(f'Администратор {session["user_id"]} удалил пост {post_id}')
        return redirect('/admin/posts')
    except Exception as e:
        app.logger.error(f'Ошибка при удалении поста {post_id}: {e}')
        return render_template('500.html'), 500

@app.route('/admin/user/delete/<int:user_id>')
@admin_required
def admin_delete_user(user_id):
    try:
        if user_id == session['user_id']:
            app.logger.warning(f'Попытка самоудаления администратором {user_id}')
            return render_template('error.html',
                                 error_code=400,
                                 error_message="Нельзя удалить самого себя"), 400
        cur.execute("SELECT name, email FROM users WHERE id = ?", [user_id])
        user = cur.fetchone()
        if not user:
            app.logger.warning(f'Попытка удаления несуществующего пользователя {user_id}')
            return render_template('404.html'), 404
        cur.execute("DELETE FROM users WHERE id = ?", [user_id])
        conn.commit()
        log_notification(session['user_id'], 'admin_user_delete',
                        f'Администратор удалил пользователя "{user[0]}" ({user[1]}, ID: {user_id})')
        app.logger.info(f'Администратор {session["user_id"]} удалил пользователя {user_id}')
        return redirect('/admin/users')
    except Exception as e:
        app.logger.error(f'Ошибка при удалении пользователя {user_id}: {e}')
        return render_template('500.html'), 500

@app.route('/admin/post/edit/<int:post_id>', methods=['GET', 'POST'])
@admin_required
def admin_edit_post(post_id):
    try:
        cur.execute('''
            SELECT posts.*, categories.name as category_name
            FROM posts 
            LEFT JOIN categories ON posts.category_id = categories.id
            WHERE posts.id = ?
        ''', [post_id])
        post = cur.fetchone()
        if not post:
            app.logger.warning(f'Попытка редактирования несуществующего поста {post_id}')
            return render_template('404.html'), 404
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            category_id = request.form.get('category')
            update_post(post_id, title, content, category_id)
            log_notification(session['user_id'], 'admin_post_edit',
                           f'Администратор отредактировал пост "{title}" (ID: {post_id})')
            app.logger.info(f'Администратор {session["user_id"]} отредактировал пост {post_id}')
            return redirect('/admin/posts')
        categories = get_all_categories()
        return render_template('admin_edit_post.html',
                             post=post,
                             categories=categories,
                             user_name=session.get('user_name'))
    except Exception as e:
        app.logger.error(f'Ошибка при редактировании поста {post_id}: {e}')
        return render_template('500.html'), 500

@app.route('/admin/user/edit/<int:user_id>', methods=['GET', 'POST'])
@admin_required
def admin_edit_user(user_id):
    try:
        user = get_user_by_id(user_id)
        if not user:
            app.logger.warning(f'Попытка редактирования несуществующего пользователя {user_id}')
            return render_template('404.html'), 404
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            role = request.form.get('role')
            if email != user[2]:
                existing_user = get_user_by_email(email)
                if existing_user and existing_user[0] != user_id:
                    return render_template('admin_edit_user.html',
                                         user=user,
                                         error='Пользователь с таким email уже существует',
                                         user_name=session.get('user_name'))
            update_user(user_id, name, email, role)
            log_notification(session['user_id'], 'admin_user_edit',
                           f'Администратор отредактировал пользователя "{name}" (ID: {user_id})')
            app.logger.info(f'Администратор {session["user_id"]} отредактировал пользователя {user_id}')
            return redirect('/admin/users')
        return render_template('admin_edit_user.html',
                             user=user,
                             user_name=session.get('user_name'))
    except Exception as e:
        app.logger.error(f'Ошибка при редактировании пользователя {user_id}: {e}')
        return render_template('500.html'), 500

def api_auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Требуется аутентификация'}), 401
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Неверный формат токена'}), 401
        token = auth_header[7:]
        user_id = validate_auth_token(token)
        if not user_id:
            return jsonify({'error': 'Недействительный токен'}), 401
        g.current_user_id = user_id
        return f(*args, **kwargs)
    return decorated_function

def api_admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'current_user_id'):
            return jsonify({'error': 'Требуется аутентификация'}), 401
        if not is_admin(g.current_user_id):
            return jsonify({'error': 'Недостаточно прав'}), 403
        return f(*args, **kwargs)
    return decorated_function

@app.route('/api/v1/posts', methods=['GET'])
def api_v1_posts():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        category_id = request.args.get('category_id', type=int)
        sort_by = request.args.get('sort_by', 'created_at')
        order = request.args.get('order', 'desc')
        search_query = request.args.get('q')
        posts = get_cached_posts(page, per_page, category_id, sort_by, order, search_query)
        posts_list = []
        for post in posts:
            posts_list.append({
                'id': post[0],
                'title': post[1],
                'content': post[2],
                'author_id': post[3],
                'author_name': post[6],
                'category_id': post[4],
                'category_name': post[7] if post[7] else 'Без категории',
                'created_at': post[5],
                'excerpt': post[2][:150] + '...' if len(post[2]) > 150 else post[2]
            })
        cur.execute('SELECT COUNT(*) FROM posts')
        total = cur.fetchone()[0]
        return jsonify({
            'success': True,
            'data': posts_list,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'total_pages': (total + per_page - 1) // per_page
            },
            'filters': {
                'category_id': category_id,
                'sort_by': sort_by,
                'order': order,
                'search': search_query
            }
        })
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/posts: {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/v1/categories', methods=['GET'])
def api_v1_categories():
    try:
        cur.execute('SELECT * FROM categories ORDER BY name')
        categories = cur.fetchall()
        categories_list = []
        for cat in categories:
            categories_list.append({
                'id': cat[0],
                'name': cat[1],
                'description': cat[2]
            })
        return jsonify({
            'success': True,
            'data': categories_list
        })
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/categories: {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/v1/posts/<int:post_id>', methods=['GET'])
def api_v1_get_post(post_id):
    try:
        cur.execute('''
            SELECT posts.*, users.name, categories.name as category_name
            FROM posts 
            JOIN users ON posts.user_id = users.id
            LEFT JOIN categories ON posts.category_id = categories.id
            WHERE posts.id = ?
        ''', [post_id])
        post = cur.fetchone()
        if not post:
            return jsonify({'success': False, 'error': 'Пост не найден'}), 404
        post_data = {
            'id': post[0],
            'title': post[1],
            'content': post[2],
            'author_id': post[3],
            'author_name': post[6],
            'category_id': post[4],
            'category_name': post[7] if post[7] else 'Без категории',
            'created_at': post[5]
        }
        return jsonify({'success': True, 'data': post_data})
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/posts/{post_id}: {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/v1/login', methods=['POST'])
@limiter.limit("5 per minute")
def api_v1_login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'Нет данных'}), 400
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({'success': False, 'error': 'Email и пароль обязательны'}), 400
        user = get_user_by_email(email)
        if not user:
            return jsonify({'success': False, 'error': 'Пользователь не найден'}), 404
        if not check_password_hash(user[3], password):
            return jsonify({'success': False, 'error': 'Неверный пароль'}), 401
        token = create_auth_token(user[0], remember=True)
        update_last_login(user[0])
        log_notification(user[0], 'api_login', 'Пользователь вошел через API')
        return jsonify({
            'success': True,
            'data': {
                'user': {
                    'id': user[0],
                    'name': user[1],
                    'email': user[2],
                    'role': user[5] if len(user) > 5 else 'user'
                },
                'token': token,
                'expires_in': 30 * 24 * 60 * 60
            }
        })
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/login: {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/v1/posts', methods=['POST'])
@api_auth_required
def api_v1_create_post():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'Нет данных'}), 400
        title = data.get('title')
        content = data.get('content')
        category_id = data.get('category_id')
        if not title or not content:
            return jsonify({'success': False, 'error': 'Заголовок и содержание обязательны'}), 400
        if len(title) > 200:
            return jsonify({'success': False, 'error': 'Заголовок не может быть длиннее 200 символов'}), 400
        if len(content) > 5000:
            return jsonify({'success': False, 'error': 'Содержание не может быть длиннее 5000 символов'}), 400
        if category_id:
            cur.execute('SELECT id FROM categories WHERE id = ?', [category_id])
            if not cur.fetchone():
                return jsonify({'success': False, 'error': 'Категория не найдена'}), 404
        add_new_post(title, content, g.current_user_id, category_id)
        cur.execute('SELECT last_insert_rowid()')
        post_id = cur.fetchone()[0]
        log_notification(g.current_user_id, 'api_new_post',
                        f'Создан пост через API: "{title}"')
        app.logger.info(f'Создан новый пост через API: {post_id} пользователем {g.current_user_id}')
        return jsonify({
            'success': True,
            'data': {
                'id': post_id,
                'title': title,
                'content': content,
                'category_id': category_id,
                'author_id': g.current_user_id
            },
            'message': 'Пост успешно создан'
        }), 201
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/posts (POST): {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/v1/posts/<int:post_id>', methods=['PUT'])
@api_auth_required
def api_v1_update_post(post_id):
    try:
        cur.execute('SELECT * FROM posts WHERE id = ?', [post_id])
        post = cur.fetchone()
        if not post:
            return jsonify({'success': False, 'error': 'Пост не найден'}), 404
        is_author = post[3] == g.current_user_id
        is_admin_user = is_admin(g.current_user_id)
        if not (is_author or is_admin_user):
            return jsonify({'success': False, 'error': 'Недостаточно прав'}), 403
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'Нет данных'}), 400
        title = data.get('title', post[1])
        content = data.get('content', post[2])
        category_id = data.get('category_id', post[4])
        if category_id:
            cur.execute('SELECT id FROM categories WHERE id = ?', [category_id])
            if not cur.fetchone():
                return jsonify({'success': False, 'error': 'Категория не найдена'}), 404
        update_post(post_id, title, content, category_id)
        log_notification(g.current_user_id, 'api_update_post',
                        f'Обновлен пост через API: "{title}" (ID: {post_id})')
        app.logger.info(f'Обновлен пост через API: {post_id} пользователем {g.current_user_id}')
        return jsonify({
            'success': True,
            'data': {
                'id': post_id,
                'title': title,
                'content': content,
                'category_id': category_id
            },
            'message': 'Пост успешно обновлен'
        })
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/posts/{post_id} (PUT): {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])
@api_admin_required
def api_v1_delete_post(post_id):
    try:
        cur.execute('SELECT * FROM posts WHERE id = ?', [post_id])
        post = cur.fetchone()
        if not post:
            return jsonify({'success': False, 'error': 'Пост не найден'}), 404
        cur.execute('DELETE FROM posts WHERE id = ?', [post_id])
        conn.commit()
        log_notification(g.current_user_id, 'api_delete_post',
                        f'Удален пост через API (ID: {post_id})')
        app.logger.info(f'Удален пост через API: {post_id} администратором {g.current_user_id}')
        return jsonify({
            'success': True,
            'message': 'Пост успешно удален'
        })
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/posts/{post_id} (DELETE): {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/docs')
def api_docs():
    user_name = session.get('user_name') if 'user_id' in session else None
    return render_template('api_docs.html', user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)