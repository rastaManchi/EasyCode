from flask import Flask, render_template, request, redirect, session, g
from db import *
import os
import secrets
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from functools import wraps


load_dotenv()
from_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASSWORD")


def send_email(email_to):
    if not from_email or not password:
        print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
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
        print("Ошибка аутентификации - неверный логин или пароль")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
    return False


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


def check_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('auth_token')
        if token:
            user_id = validate_auth_token(token)
            if user_id:
                user = get_user_by_id(user_id)
                session['user_id'] = user[0]
                session['username'] = user[1]
        username = None
        if 'user_id' in session:
            username = session['username']
        g.username = username
        res = func(*args, **kwargs)
        return res
    return wrapper


#http://127.0.0.1:5000/test
@app.route('/test')
def test():
    return render_template('test.html')


#http://127.0.0.1:5000/
@app.route('/')
@check_session
def home():
    posts = get_all_posts()
    users = get_all_users()
    return render_template('main.html', posts=posts, users=users, username=g.username)


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
def new_post():
    return render_template('new_post.html')


@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_new_post(title, content)
    return redirect('/')


#http://127.0.0.1:5000/login
@app.route('/login', methods=['GET', 'POST'])
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
            return "Wrong password"
        return "User not found"
    return render_template('login.html')


#http://127.0.0.1:5000/register
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
            email_send = send_email(email_to=email)
            if email_send:
                log_notification(user[0], 'welcome_email_sent', f'Приветственное письмо отправлено на {email}')
            else:
                log_notification(user[0], 'welcome_email_sent', f'Приветственное письмо НЕ было отправлено на {email}')
            return render_template('profile.html')
    return render_template('register.html')


app.run()
