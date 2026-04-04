from flask import Flask, render_template, request, redirect, session, jsonify
from db import *
from dotenv import load_dotenv
from email.mime.text import MIMEText
import os
import smtplib

import secrets

# Логи
import traceback
import logging
from logging.handlers import RotatingFileHandler

load_dotenv()


if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler(
    'logs/name.log',
    maxBytes=10240,
    backupCount=10,
    encoding='utf-8'
)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)


def send_gmail_message(user_email):
    from_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")
    if not from_email or not password:
        print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
        return False
    subject = "Добро пожаловать"
    body = """Привет, это тестовое сообщение!"""
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = user_email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        return True
    except smtplib.SMTPAuthenticationError:
        print("Ошибка аутентификации - неверный логин или пароль")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
    return False


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.errorhandler(404)
def error_404(error):
    if app.debug:
        error_traceback = traceback.format_exc()
        return render_template('debug_error.html',
                               error_type=type(error).__name__,
                               error_message=str(error),
                               error_traceback=error_traceback), 404
    app.logger.error(error)
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_500(error):
    app.logger.error(error)
    return render_template('500.html'), 500


@app.route('/test500')
def test500():
    raise Exception("Описание ошибки")


@app.route('/debugtest')
def debug_test():
    result = 10/0
    return str(result)


@app.route('/')
def home():
    page_num = int(request.args.get('page_num', 1))
    posts_offset = (page_num - 1) * 5
    total_posts = get_all_posts_count()
    total_pages = total_posts // 5 + 1
    
    all_posts = get_posts_by_page(posts_offset)
    all_users = get_all_users()
    if 'user_id' not in session:
        token = request.cookies.get('auth_token')
        if token:
            user_id = validate_auth_token(token)
            if user_id:
                user = get_user_by_id(user_id)
                if user:
                    session['user_id'] = user[0]
                    session['username'] = user[1]
    username = None
    if 'user_id' in session:
        username = session['username']
    return render_template('main.html',
                           all_users=all_users,
                           all_posts=all_posts,
                           username=username,
                           page_num=page_num,
                           total_pages=total_pages)
    
    
@app.route('/api/posts')
def api_posts():
    page_num = int(request.args.get('page_num', 1))
    posts_offset = (page_num - 1) * 5
    all_posts = get_posts_by_page(posts_offset)
    result = []
    for post in all_posts:
        result.append({
            'id': post[0],
            'title': post[1],
            'content': post[2],
            'author': post[3]
        })
    return jsonify(result)


@app.route('/search_post', methods=["GET"])
def search_post():
    data = request.args
    search_text = data.get('search_text')
    posts = get_posts_by_text(search_text)
    all_users = get_all_users()
    if 'user_id' not in session:
        token = request.cookies.get('auth_token')
        if token:
            user_id = validate_auth_token(token)
            if user_id:
                user = get_user_by_id(user_id)
                if user:
                    session['user_id'] = user[0]
                    session['username'] = user[1]
    username = None
    if 'user_id' in session:
        username = session['username']
    return render_template('main.html', all_users=all_users, all_posts=posts, username=username), 200


#http://127.0.0.1:5000/user/1
@app.route('/user/<int:user_id>')
def user(user_id):
    print(type(user_id))
    user = get_user_by_id(user_id)
    user_posts = get_posts_by_user(user_id)
    # 2.1 TODO: Получить все уведы пользователя
    if user:
        # 2.2 TODO: передать в return все уведы пользователя
        return render_template('user_template.html', user=user, user_posts=user_posts)
    return f"Пользователь не найден", 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        remember = data.get('remember')
        user = get_user_by_email(email)
        if user:
            user_pass = user[3]
            if user_pass == password:
                session['user_id'] = user[0]
                session['username'] = user[1]
                log_notification(user[0], 'login', 'Успешная авторизация')
                if remember:
                    token = create_auth_token(user[0], True)
                    response = redirect('/')
                    response.set_cookie('auth_token', token, max_age=60*60*24*30)
                else:
                    response = redirect('/')
                return response, 301
            return "Неверный пароль", 401
        return "Неверная почта", 401
    return render_template('login.html'), 200


@app.route('/logout')
def logout():
    user_id = session.get('user_id')
    session.clear()
    delete_auth_token(user_id)
    return redirect('/'), 301


@app.route('/register', methods=['GET', 'POST'])
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
            email_sent = send_gmail_message(email)
            if email_sent:
                log_notification(user[0], 'welcome_email_sent', f'Письмо успешно отправлено на {email}')
            else:
                log_notification(user[0], 'welcome_email_sent', f'Письмо не было отправлено на {email}')
            return "Успешно", 201
        return "Пользователь уже существует", 409
    return render_template("register.html"), 200


@app.route('/post')
def post():
    return render_template('new_posts.html')


@app.route('/add_post', methods=['POST'])
def add_post():
    user_id = session.get('user_id')
    if user_id:
        data = request.form
        title = data.get('title')
        content = data.get('content')
        add_post_to_db(title, content, user_id)
        return redirect('/')
    return "Вы не авторизованы", 401


app.run('0.0.0.0', 8000, debug=False)