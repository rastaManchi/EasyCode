from flask import Flask, render_template, request, redirect, session, jsonify
from db import*
import secrets
import os
import smtplib
from email.mime.text import MIMEText

import traceback
import logging
from logging.handlers import RotatingFileHandler

if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler(
    'logs/blog.log',
    maxBytes=10240,
    backupCount=5,
    encoding='utf-8'
)
format_logger = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
file_handler.setFormatter(format_logger)
file_handler.setLevel(logging.INFO)

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


def send_message(email_to):
    if not EMAIL_LOGIN or not EMAIL_PASSWORD:
        print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
        exit()
    subject = "Добро пожаловать!"
    body = """
Привет, рады видеть тебя на нашем сайте!
    """
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = EMAIL_LOGIN
    msg['To'] = email_to
    try:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print("Ошибка аутентификации - неверный логин или пароль")
    except Exception as e:
        print(f"Ошибка подключения: {e}")


@app.route('/')
def hello_world():
    posts = get_all_post()
    users = get_all_users()
    user_id = None
    user_name = None
    if 'user_id' in session:
        user_id = session['user_id']
        user_name = session['user_name']
    return render_template('main.html',posts = posts , users = users, user_id = user_id, user_name = user_name)
    

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = get_user_by_email(email)

        if user is None:
            add_user(name,email, password)
            user = get_user_by_email(email)
            session["user_id"]=user[0]
            session["user_name"]=user[1]
            send_message(email)
            return redirect('/profile')
        else:
            print('Такой пользователь уже существует')

    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = get_user_by_email(email)
        if user is None:
             return render_template('login.html', message="Нет такой почты")
        
        if user[3] == password:
            print('Вход выполнен')
            session['user_id'] = user[0]
            session['user_name'] = user[1]

            return redirect('/profile')
        else:
            return render_template('login.html', message="Пароль неверный")
        
    return render_template('login.html')

@app.route('/add_post',methods=['GET','POST'])
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        category_id = request.form.get('category')
        if 'user_id' in session:
            user_id = session['user_id']
        else:
            return redirect('/login/')
        new_post(title, content, user_id, category_id)
        return redirect('/')
    categories = get_all_categories()
    return render_template('new_post.html', categories=categories) 

@app.route('/user/<int:user_id>')
def user_page(user_id):
    user = get_user_by_id(user_id)
    posts = get_posts_by_user(user_id)
    if  user:
        return render_template('user_page.html', user=user, posts=posts)
    return "Пользователь не найден", 404

@app.route("/search")
def search():
    query = request.args.get('q', '')
    users = get_all_users()
    user_id = None
    user_name = None
    if 'user_id' in session:
        user_id = session['user_id']
        user_name = session['user_name']

    posts = search_posts(query)
    return render_template('main.html',posts = posts , users = users, user_id = user_id, user_name = user_name)


@app.route('/api/v1/posts')
def api_posts():
    posts = get_all_post()
    # result = []
    # for post in posts:
    #     result.append({
    #         'id': post[0],
    #         'title': post[1],
    #         'content': post[2]
    #     })
    return jsonify(posts)


@app.route('/test500')
def test_500():
    raise Exception('Это тестовая 500 ошибка!')


@app.errorhandler(404)
def error_404(error_text):
    app.logger.warning(f"404 Ошибка - {error_text}")
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_500(error_text):
    app.logger.warning(f"500 Ошибка - {error_text}")
    return render_template('500.html'), 500


app.run(debug=True)