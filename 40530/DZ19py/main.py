from flask import Flask, render_template, request, redirect, make_response, jsonify, g
from db import *
from functools import wraps
import secrets
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'ваш-секретный-ключ'  # Измените на реальный секретный ключ

# Вспомогательные функции
def validate_auth_token(token):
    """Проверка токена аутентификации"""
    result = check_token(token)
    if result:
        return result[3]
    else:
        return None


def create_auth_token(user_id, remember=False):
    """Создание токена аутентификации"""
    
    token = secrets.token_urlsafe(32)
    while check_token(token):
        token = secrets.token_urlsafe(32)
    expires = datetime.now() + timedelta(days=30 if remember else 1)
    create_token(user_id, token)
    return token    


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


@app.route('/api/home')
@api_auth_required
def home():
    return jsonify({'status': 'Успех'})


@app.route('/api/login', methods=['POST'])
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
        if user[0][3] != password:
            return jsonify({'success': False, 'error': 'Неверный пароль'}), 401
        
        token = create_auth_token(user[0][0], remember=True)
        # update_last_login(user['id'])
        # log_notification(user['id'], 'api_login', 'Пользователь вошел через API')
        
        return jsonify({
            'success': True,
            'data': {
                'user': {
                    'id': user[0][0],
                    'name': user[0][1],
                    'email': user[0][2],
                    'role': 'admin' if user[0][4] else 'user'
                },
                'token': token,
                'expires_in': 30 * 24 * 60 * 60
            }
        })
        
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/login: {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500


@app.route('/')
def welcome():
    posts = get_posts()
    id = request.cookies.get('session')
    is_admin = False
    if id:
        try:
            user = get_user_by_id(id)
            is_admin = user[4]
        except:
            pass
    return render_template('main.html', posts = posts, is_admin = is_admin)

@app.route('/api/posts')
@api_auth_required
def welcome_api():
    print(g.current_user_id)
    posts = get_posts()
    return jsonify(posts)


@app.route('/admin_p/', methods = ['GET', 'POST'])
def admin_p():
    id = request.cookies.get('session')
    is_admin = False
    if id:
        user = get_user_by_id(id)
        is_admin = user[4]
        if is_admin:
            zero_posts = search_zero_posts()
            return render_template('admin.html', zero_posts = zero_posts)
    return redirect('/')

@app.route('/approve/<int:post_id>', methods = ['GET', 'POST'])
def approve(post_id):
    id = request.cookies.get('session')
    is_admin = False
    if id:
        user = get_user_by_id(id)
        is_admin = user[4]
        if is_admin:
            status_post_approve(post_id)
    return redirect('/admin_p')


@app.route('/api/post', methods=['PUT'])
@api_auth_required
@api_admin_required
def approve_api():
    try:
        data = request.get_json()
        post_id = data.get('post_id')
        if post_id:
            status_post_approve(post_id)
            return jsonify({'status': 'success'})
        return jsonify({'status': 'failed'}), 404
    except Exception as e:
        app.logger.error(f'Ошибка в API v1/login: {e}')
        return jsonify({'success': False, 'error': 'Внутренняя ошибка сервера'}), 500

    
@app.route('/disapprove/<int:post_id>', methods = ['GET', 'POST'])
def disapprove(post_id):
    id = request.cookies.get('session')
    is_admin = False
    if id:
        user = get_user_by_id(id)
        is_admin = user[4]
        if is_admin:
            status_post_disapprove(post_id)
    return redirect('/admin_p')


@app.route('/register/', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form 
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        user = get_user_by_email(email)
        if user:
            print('Такой пользователь существует')
        else:
            add_user(name, email, password)
            user = get_user_by_email(email)
            response = make_response(redirect('/profile/'))
            response.set_cookie('session', str(user[0][0]), 6000)
            return response
    return render_template('register.html')

@app.route('/profile/')
def profile():
    return render_template('profile.html')


@app.route('/api/profile')
@api_auth_required
def api_profile():
    user = get_user_by_id(g.current_user_id)
    return jsonify({
        "id": user[0],
        "name": user[1]
    })


@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')

        user = get_user_by_email(email)
        if user:
            if password == user[0][3]:
                response = make_response(redirect('/profile/'))
                response.set_cookie('session', str(user[0][0]), 6000)
                return response
            else:
                print('Пароль неверный!')
        else:
            print('Пользователя не существует!')
    return render_template('login.html')

@app.route('/add_post/', methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        data = request.form
        title = data.get('title')
        content = data.get('content')
        add_post_in_db(title, content)
        return redirect('/profile/') 
    return render_template('add_post.html')

@app.route('/Search/', methods=['GET', 'POST'])
def but_Search():
    if request.method == 'POST':
        data = request.form
        search = data.get('Text')
        posts = search_post(search)
        return posts


if __name__ == '__main__':
    app.run()