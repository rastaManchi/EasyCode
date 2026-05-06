from flask import Flask, render_template, request, redirect, session, g, jsonify
from db import *
import os
import secrets
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from functools import wraps

import traceback
import logging
from logging.handlers import RotatingFileHandler

if not os.path.exists('logs'):
    os.mkdir('logs')
    
file_handler = RotatingFileHandler('logs/app.log',
                                   maxBytes=10240,
                                   backupCount=10,
                                   encoding='utf-8')
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s : %(lineno)d]'
))
file_handler.setLevel(logging.INFO)

load_dotenv()
from_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASSWORD")


def send_email(email_to):
    if not from_email or not password:
        app.logger.error("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
        exit()
    subject = "Добро пожаловать в наш блог!"
    body = f"""
Привет,
Спасибо за регистрацию
С уважением, наша команда <3
    """
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = email_to
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        return True
    except smtplib.SMTPAuthenticationError:
        app.logger.error("Ошибка аутентификации - неверный логин или пароль")
    except Exception as e:
        app.logger.error(f"Ошибка подключения: {e}")
    return False


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info("Сайт запущен")


def check_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('auth_token')
        g.user_id = None
        if token:
            user_id = validate_auth_token(token)
            if user_id:
                user = get_user_by_id(user_id)
                session['user_id'] = user[0]
                session['username'] = user[1]
                g.user_id = user_id
        username = None
        if 'user_id' in session:
            username = session['username']
        g.username = username
        res = func(*args, **kwargs)
        return res
    return wrapper


def check_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session['user_id']
        print(user_id)
        user = get_user_by_id(user_id)
        if user[4]:
            result = func(*args, **kwargs)
            return result
        else:
            return redirect('/'), 403
    return wrapper


def api_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'status': 'failed', 'msg': 'Не указан Authorization'}), 401
        is_valid = validate_api_token(auth_header)
        if not is_valid:
            return jsonify({'status': 'failed', 'msg': 'Неверный Authorization'}), 401
        result = func(*args, **kwargs)
        add_api_request(auth_header)
        return result
    return wrapper


#http://127.0.0.1:5000/test
@app.route('/test')
def test():
    return render_template('test.html')


#http://127.0.0.1:5000/
@app.route('/')
@check_session
def home():
    current_page = int(request.args.get('page', 1))
    posts_per_page = 2
    posts_count = get_posts_count()
    pages = posts_count // posts_per_page + 1
    offset = posts_per_page * (current_page - 1)
    posts = get_all_posts_by_page(posts_per_page, offset)
    user = get_user_by_id(g.user_id)
    admin = False
    if user[4]:
        admin = True
    users = get_all_users()
    return render_template('main.html',
                           posts=posts,
                           users=users,
                           username=g.username,
                           current_page=current_page,
                           pages=pages,
                           isadmin=admin)


@app.route('/loadposts')
def loadposts():
    current_page = int(request.args.get('page', 1))
    posts_per_page = 2
    offset = posts_per_page * (current_page - 1)
    posts = get_all_posts_by_page(posts_per_page, offset)
    posts_data = []
    for post in posts:
        posts_data.append({
            'id': post[0],
            'title': post[1],
            'content': post[2],
            'user_id': post[3]
        })
    return jsonify(posts_data), 200


@app.route('/search')
@check_session
def search():
    data = request.args
    q = data.get('q')
    posts = get_posts_by_text(q)
    users = get_all_users()
    return render_template('main.html', posts=posts, users=users, username=g.username)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/user/<int:user_id>')
@check_session
def get_user_profile(user_id):
    user = get_user_by_id(user_id)
    posts = get_posts_by_user_id(user_id)
    notifications = get_notifications_by_user_id(user_id)
    if user:
        return render_template('user_page.html',
                            user=user,
                            posts=posts,
                            notifications=notifications)
    return "Пользователь не найден", 404


@app.route('/new_post')
@check_session
def new_post():
    return render_template('new_post.html')


@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_new_post(title, content)
    return redirect('/')


@app.route('/admin/post/edit/<int:post_id>', methods=['GET', 'POST'])
@check_session
@check_admin
def edit_post(post_id):
    post = get_post_by_id(post_id)
    if request.method == 'POST':
        data = request.form
        new_title = data.get('title')
        new_content = data.get('content')
        update_post(post_id, new_title, new_content)
        return redirect('/')
    return render_template('edit_post.html',
                           title = post[1],
                           content = post[2])


#http://127.0.0.1:5000/login
@app.route('/login', methods=['GET', 'POST'])
@check_session
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        remember = data.get('remember')
        user = get_user_by_email(email)
        if user:
            if user[3] == password:
                session['user_id'] = user[0]
                session['username'] = user[1]
                if remember:
                    token = create_auth_token(user[0], True)
                    response = redirect('/')
                    response.set_cookie('auth_token', token, max_age=60 * 60 * 24 * 30)
                else:
                    response = redirect('/')
                return response
            return "Wrong password", 403
        return "User not found", 404
    if g.username:
        return redirect('/'), 301
    return render_template('login.html')


#http://127.0.0.1:5000/register
@app.route('/register', methods=['GET', 'POST'])
@check_session
def register():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        user = get_user_by_email(email)
        if not user:
            add_user(name, email, password)
            user = get_user_by_email(email)
            email_send = send_email(email_to=email)
            if email_send:
                log_notification(user[0], 'welcome_email_sent', f'Приветственное письмо отправлено на {email}')
            else:
                log_notification(user[0], 'welcome_email_sent', f'Приветственное письмо НЕ было отправлено на {email}')
            return render_template('profile.html')
    if g.username:
        return redirect('/')
    return render_template('register.html')


@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = get_user_by_email(email)
    if user and user[3] == password:
        token = create_token(user[0])
        return jsonify({
            'status': 'success',
            'msg': 'Токен создан',
            'auth_token': token
        })
    return jsonify({
            'status': 'failed',
            'msg': 'Ошибка авторизации'
        }), 401


# http://127.0.0.1:5000/api/posts?page=1
@app.route('/api/posts')
@api_check
def api_posts():
    current_page = int(request.args.get('page', 1))
    posts_per_page = 2
    offset = posts_per_page * (current_page - 1)
    posts = get_all_posts_by_page(posts_per_page, offset)
    data = []
    for post in posts:
        data.append({
            "id": post[0],
            "title": post[1],
            "content": post[2],
            "author": post[3],
            "status": post[4]
        })
    return jsonify({
        'status': 'success',
        'msg': 'Is OK :)',
        'data': data
    })
    
    
@app.route('/api/users/<int:user_id>')
@api_check
def api_user_info(user_id):
    user = get_user_by_id(user_id)
    data_user = {
        'id': user[0],
        'name': user[1],
        'email': user[2],
        'is_admin': user[4]
    }
    posts = get_posts_by_user_id(user_id)
    data_posts = []
    for post in posts:
        data_posts.append({
            "id": post[0],
            "title": post[1],
            "content": post[2],
            "author": post[3],
            "status": post[4]
        })
    notifications = get_notifications_by_user_id(user_id)
    data_notifications = []
    for notification in notifications:
        data_notifications.append({
            "id": notification[0],
            "user_id": notification[1],
            "action": notification[2],
            "details": notification[3],
            "created_at": notification[4]
        })
    if user:
        return jsonify({
            'status': 'successed',
            'msg': '',
            'user': data_user,
            'posts': data_posts,
            'notifications': data_notifications
        })
    return jsonify({
        'status': 'failed',
        'msg': 'Пользователь не найден'
    }), 404


@app.route('/admin')
@check_session
@check_admin
def admin():
    zeroposts = get_status_posts(0)
    approveposts = get_status_posts(1)
    disapproveposts = get_status_posts(2)
    return render_template('admin.html', 
                           zeroposts=zeroposts,
                           approveposts=approveposts,
                           disapproveposts=disapproveposts)
    
@app.route('/approve')
@check_session
@check_admin
def approve():
    id = request.args.get('id')
    set_post_status(id, 1)
    return redirect('/admin')


@app.route('/disapprove')
@check_session
@check_admin
def disapprove():
    id = request.args.get('id')
    set_post_status(id, 2)
    return redirect('/admin')


@app.route('/error500')
def error_500_test():
    raise Exception("Это тестовая 500 ошибка!!!")


@app.errorhandler(404)
def error_404(error):
    app.logger.error(error)
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_500(error):
    app.logger.error(error)
    return render_template('500.html'), 500


@app.route('/docs')
def docs():
    return render_template('docs.html')


if __name__ == '__main__':
    app.run()
