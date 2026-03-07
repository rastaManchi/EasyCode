from flask import Flask, render_template, request, redirect, session, jsonify, g
import sqlite3
from functools import wraps
import hashlib
import secrets
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'ваш-секретный-ключ'  # Измените на реальный секретный ключ

# Подключение к базе данных
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Вспомогательные функции
def validate_auth_token(token):
    """Проверка токена аутентификации"""
    # Здесь должна быть реальная проверка токена
    # Для примера возвращаем ID пользователя
    try:
        # Раскодируем токен и проверяем его
        return 1  # В реальности нужно проверять токен в БД
    except:
        return None

def is_admin(user_id):
    """Проверка прав администратора"""
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT is_admin FROM users WHERE id = ?', [user_id])
    user = cur.fetchone()
    return user and user['is_admin'] == 1

def get_cached_posts(page, per_page):
    """Получение постов с пагинацией"""
    db = get_db()
    cur = db.cursor()
    offset = (page - 1) * per_page
    cur.execute('''
        SELECT p.*, u.name as author_name, c.name as category_name 
        FROM posts p
        JOIN users u ON p.user_id = u.id
        LEFT JOIN categories c ON p.category_id = c.id
        ORDER BY p.created_at DESC
        LIMIT ? OFFSET ?
    ''', [per_page, offset])
    return cur.fetchall()

def create_auth_token(user_id, remember=False):
    """Создание токена аутентификации"""
    token = secrets.token_urlsafe(32)
    expires = datetime.now() + timedelta(days=30 if remember else 1)
    # Здесь нужно сохранить токен в БД
    return token

def update_last_login(user_id):
    """Обновление времени последнего входа"""
    db = get_db()
    cur = db.cursor()
    cur.execute('UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?', [user_id])
    db.commit()

def log_notification(user_id, action, message):
    """Логирование действий пользователя"""
    db = get_db()
    cur = db.cursor()
    cur.execute('''
        INSERT INTO notifications (user_id, action, message, created_at)
        VALUES (?, ?, ?, CURRENT_TIMESTAMP)
    ''', [user_id, action, message])
    db.commit()

def get_user_by_email(email):
    """Получение пользователя по email"""
    db = get_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM users WHERE email = ?', [email])
    return cur.fetchone()

def add_new_post(title, content, user_id, category_id=None):
    """Добавление нового поста"""
    db = get_db()
    cur = db.cursor()
    cur.execute('''
        INSERT INTO posts (title, content, user_id, category_id, created_at)
        VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
    ''', [title, content, user_id, category_id])
    db.commit()

def update_post(post_id, title, content, category_id=None):
    """Обновление поста"""
    db = get_db()
    cur = db.cursor()
    cur.execute('''
        UPDATE posts 
        SET title = ?, content = ?, category_id = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    ''', [title, content, category_id, post_id])
    db.commit()

# Декораторы
def api_auth_required(f):
    """Декоратор для проверки аутентификации в API"""
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
    """Декоратор для проверки прав администратора в API"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not hasattr(g, 'current_user_id'):
            return jsonify({'error': 'Требуется аутентификация'}), 401
        
        if not is_admin(g.current_user_id):
            return jsonify({'error': 'Недостаточно прав'}), 403
        
        return f(*args, **kwargs)
    return decorated_function

# API Endpoints
@app.route('/api/v1/posts', methods=['GET'])
def api_v1_posts():
    """API для получения постов (версия 1)"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        posts = get_cached_posts(page, per_page)
        
        posts_list = []
        for post in posts:
            content = post['content'] if 'content' in post else ''
            excerpt = content[:150] + '...' if len(content) > 150 else content
            
            posts_list.append({
                'id': post['id'],
                'title': post['title'],
                'content': content,
                'author_id': post['user_id'],
                'author_name': post['author_name'],
                'category_id': post['category_id'],
                'category_name': post['category_name'] if post['category_name'] else 'Без категории',
                'created_at': post['created_at'],
                'excerpt': excerpt
            })
        
        db = get_db()
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) as total FROM posts')
        total = cur.fetchone()['total']
        
        return jsonify({
            'success': True,
            'data': posts_list,
            'pagination': {
                'page': page,
                'per_page': per_page,
                'total': total,
                'total_pages': (total + per_page - 1) // per_page
            }
        })
        
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/posts: {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/v1/posts/<int:post_id>', methods=['GET'])
def api_v1_get_post(post_id):
    """API для получения конкретного поста"""
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('''
            SELECT p.*, u.name as author_name, c.name as category_name
            FROM posts p
            JOIN users u ON p.user_id = u.id
            LEFT JOIN categories c ON p.category_id = c.id
            WHERE p.id = ?
        ''', [post_id])
        
        post = cur.fetchone()
        
        if not post:
            return jsonify({'success': False, 'error': 'Пост не найден'}), 404
        
        post_data = {
            'id': post['id'],
            'title': post['title'],
            'content': post['content'],
            'author_id': post['user_id'],
            'author_name': post['author_name'],
            'category_id': post['category_id'],
            'category_name': post['category_name'] if post['category_name'] else 'Без категории',
            'created_at': post['created_at']
        }
        
        return jsonify({'success': True, 'data': post_data})
        
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/posts/{post_id}: {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

@app.route('/api/v1/login', methods=['POST'])
def api_v1_login():
    """API для входа и получения токена"""
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
        
        # В реальном проекте используйте хеширование паролей
        if user['password'] != password:
            return jsonify({'success': False, 'error': 'Неверный пароль'}), 401
        
        token = create_auth_token(user['id'], remember=True)
        update_last_login(user['id'])
        log_notification(user['id'], 'api_login', 'Пользователь вошел через API')
        
        return jsonify({
            'success': True,
            'data': {
                'user': {
                    'id': user['id'],
                    'name': user['name'],
                    'email': user['email'],
                    'role': 'admin' if user.get('is_admin') else 'user'
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
    """API для создания нового поста"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'success': False, 'error': 'Нет данных'}), 400
        
        title = data.get('title')
        content = data.get('content')
        category_id = data.get('category_id')
        
        if not title or not content:
            return jsonify({'success': False, 'error': 'Заголовок и содержание обязательны'}), 400
        
        if category_id:
            db = get_db()
            cur = db.cursor()
            cur.execute('SELECT id FROM categories WHERE id = ?', [category_id])
            if not cur.fetchone():
                return jsonify({'success': False, 'error': 'Категория не найдена'}), 404
        
        add_new_post(title, content, g.current_user_id, category_id)
        
        db = get_db()
        cur = db.cursor()
        cur.execute('SELECT last_insert_rowid() as id')
        post_id = cur.fetchone()['id']
        
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
    """API для обновления поста"""
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('SELECT * FROM posts WHERE id = ?', [post_id])
        post = cur.fetchone()
        
        if not post:
            return jsonify({'success': False, 'error': 'Пост не найден'}), 404
        
        # Проверка прав
        is_author = post['user_id'] == g.current_user_id
        is_admin_user = is_admin(g.current_user_id)
        
        if not (is_author or is_admin_user):
            return jsonify({'success': False, 'error': 'Недостаточно прав'}), 403
        
        data = request.get_json()
        
        if not data:
            return jsonify({'success': False, 'error': 'Нет данных'}), 400
        
        title = data.get('title', post['title'])
        content = data.get('content', post['content'])
        category_id = data.get('category_id', post['category_id'])
        
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
    """API для удаления поста (только для администраторов)"""
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute('SELECT * FROM posts WHERE id = ?', [post_id])
        post = cur.fetchone()
        
        if not post:
            return jsonify({'success': False, 'error': 'Пост не найден'}), 404
        
        cur.execute('DELETE FROM posts WHERE id = ?', [post_id])
        db.commit()
        
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
    """Страница с документацией API"""
    user_name = session.get('user_name') if 'user_id' in session else None
    return render_template('api_docs.html', user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)