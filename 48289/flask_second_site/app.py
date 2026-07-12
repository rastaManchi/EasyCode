from flask import Flask, render_template, request, redirect, session, jsonify
from db import *
from dotenv import load_dotenv
load_dotenv()
import smtplib
import os
from email.mime.text import MIMEText
import secrets


EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_message(email_to):
    if not EMAIL_LOGIN or not EMAIL_PASSWORD:
        print("ОШИБКА: Не найдены EMAIL_LOGIN или EMAIL_PASSWORD в .env файле!")
        exit()
    subject = "Добро пожаловать!"
    body = """
привествую тебя :)
    """
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = EMAIL_LOGIN
    msg['To'] = email_to
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
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


@app.route('/')
def home():
    all_posts = get_all_posts()
    all_users = get_all_users()
    if not session:
        auth_token = request.cookies.get('auth_token')
        if auth_token:
            user_id = validate_auth_token(auth_token)
            if user_id:
                user = get_user_by_id(user_id)
                session['user_id'] = user[0]
                session['user_name'] = user[1]
    user_name = session.get('user_name')
    return render_template('home.html', 
                           posts=all_posts,
                           users=all_users,
                           user_name=user_name)


@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = get_user_by_id(user_id)
    posts = get_posts_by_user(user_id)
    logs_notifications = get_logs_notifications_by_user(user_id)
    if user:
        return render_template('profile.html',
                               user=user,
                               posts=posts,
                               logs_notifications=logs_notifications)
    return "Пользователь не найден", 404


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        user = get_user_by_email(email)
        if user and user[3] == password:
            add_log_notification(user[0],
                                 'auth',
                                 'Успешная авторизация')
            session['user_id'] = user[0]
            session['user_name'] = user[1]
            token = create_auth_token(user[0])
            response = redirect('/')
            response.set_cookie('auth_token', token, 600)
            return response
        return 'Неверные данные'
    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        user_name = data.get('name')
        user_email = data.get('email')
        user_password = data.get('password')
        if user_name and user_email and user_password:
            user = get_user_by_email(user_email)
            if not user:
                create_user(user_name, user_email, user_password)
                user = get_user_by_email(user_email)
                if send_message(user_email):
                    add_log_notification(user[0],
                                         'email_send',
                                         'Успешно отправлено на почту')
                else:
                    add_log_notification(user[0],
                                         'email_send',
                                         'Отправка сообщения на почту не удалась')
                return "Пользователь создан"
    return render_template('signup.html')


@app.route('/new_post')
def new_post():
    return render_template('add_post.html')


@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    create_post(title, content)
    return redirect('/')

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    login = data.get('login')
    password = data.get('password')
    user = get_user_by_email(login)
    if user:
        if user[3] == password:
            token = create_api_token(user[0])
            return jsonify({
                'status': 'successed',
                'token': token
            })
    return jsonify({
        'status': 'failed'
    }), 401

@app.route('/api/users')
def api_users():
    api_token = request.headers.get('Authorization')
    if not api_token:
        return jsonify({
            'status': 'failed',
            'msg': 'Токен не указан'
        }), 401
    if not validate_api_token(api_token):
        return jsonify({
            'status': 'failed',
            'msg': 'Токен не валиден'
        }), 401
    return jsonify({
        'status': 'successed'
    })



@app.errorhandler(404)
def error_404(e):
    return "404Error", 401

if __name__ == '__main__':
    app.run()
