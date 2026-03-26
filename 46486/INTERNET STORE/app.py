from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   session)
from db import *
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
import secrets


load_dotenv()


def send_mail(to_email, username):
    from_email = os.getenv("MAIL_LOGIN")
    password = os.getenv("MAIL_PASSWORD")
    if not from_email or not password:
        print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
        exit()
    
    subject = "Добро пожаловать в наш блог!"
    body = f"Привет, {username}\nСпасибо за регистрацию!"
        
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print("Ошибка аутентификации - неверный логин или пароль")
    except Exception as e:
        print(f"Ошибка подключения: {e}")


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/')
def main():
    token = request.cookies.get('auth_token')
    if token:
        user_id = validate_token(token)
        if user_id:
            user = get_user_by_id(user_id)
            session['user_id'] = user[0]
            session['username'] = user[1]
    
    username = session.get('username')
    return render_template('main.html', username=username)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = get_user_by_email(email)

        if user is None:
            add_user(name, email, password)
            send_mail(email, name)
            return redirect('/profile/')
        else:
            print('Такой пользователь уже есть')

    return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = get_user_by_email(email)
        if user is None:
            return render_template('login.html', message="Нет такой почты")
        if user[3] == password:
            print('Вход выполнен')
            token = create_token(user[0])
            session['user_id'] = user[0]
            session['username'] = user[1]
            result = redirect('/profile/')
            result.set_cookie('auth_token',
                              token,
                              60 * 10)
            return result   
        else:
            return render_template('login.html', message="Пароль неверный")
    return render_template('login.html')


@app.route('/new_post/')
def new_post():
    return render_template('new_post.html')


@app.route('/add_post/', methods=['POST'])
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_posts(title, content)
    return "Пост добавлен"


@app.route('/user/<int:user_id>')
def user(user_id):
    user = get_user_by_id(user_id)
    if user:
        posts = get_posts_by_user_id(user_id)
        return render_template('profile.html', posts=posts, user=user)
    return "Пользователь не найден!", 404


if __name__=='__main__':
    app.run(debug=True)