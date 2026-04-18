from flask import Flask, render_template, request, redirect
from db import *
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
load_dotenv()


app = Flask(__name__)

from_email = os.getenv("MAIL_LOGIN")
password = os.getenv("MAIL_PASSWORD")

def send_mail(email):
    if not from_email or not password:
        print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
        exit()
        
    subject = f'Добро пожаловать в наш блог'
    body = f'Рады вас приветствовать!!!'
    
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['To'] = email
    msg['From'] = from_email
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        
        server.send_message(msg)
        
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print("Ошибка аутентификации - неверный логин или пароль")
    except Exception as e:
        print(f"Ошибка подключения: {e}")


@app.route('/')
def home():
    posts = get_posts()
    return render_template('home.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        user = get_user_by_email(email)
        if user:
            if user[3] == password:
                return "Успешная авторизация"
        return "логин или пароль неверный"
    return render_template('login.html')


@app.route('/register')
def register():
    data = request.args # {'username': 'Булат', 'email': 'admin@admin', 'password': 'password'}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if username:
        user = get_user_by_email(email)
        if not user:
            create_user(username, email, password)
            send_mail(email)
            return "Успешная регистрация"
        return "Пользователь уже существует"
    return render_template('register.html')


@app.route('/logout')
def logout():
    pass


@app.route('/post')
def post():
    return render_template('new_post.html')


@app.route('/add_post', methods=['POST'])
def add_post_to_db():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_post(title, content)
    return redirect('/')


@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = get_user_by_id(user_id)
    username = user[1]
    email = user[2]
    posts = get_posts_by_author(user_id)
    
    return render_template('profile.html',
                           username=username,
                           email=email,
                           posts=posts)


if __name__ == '__main__':
    app.run()
