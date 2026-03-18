from flask import Flask, render_template, redirect, request, make_response
from help import *
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText


load_dotenv()
from_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASSWORD")


def send_mail(email_to):
    if not from_email or not password:
        print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
        return False
    subject = "Добро пожаловать!"
    body = """
Добрый день!
Спасибо, что выбрали нас!

Команда ... <3
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

@app.route('/')
def main():
    user_id = request.cookies.get('user_id') 
    user = get_user_by_id(user_id) 
    posts = get_all_posts()
    users = get_all_users()
    return render_template('main.html', posts = posts, users=users)


@app.route('/profile/<int:user_id>')
def profile(user_id):
    posts = get_posts_by_user_id(user_id)
    return render_template('profile.html', posts=posts)

@app.route('/new_post')
def new_post():   
    return render_template('new_post.html') 

@app.route('/add_post', methods = ["POST"])
def post():
    user_id = request.cookies.get('user_id') 
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_new_post(title, content, user_id)
    return redirect('/')

@app.route('/register', methods= ["GET", "POST"])
def register():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')
        add_user(name, email, password)
        user = get_user_by_email(email)
        send_mail(email)
        response = make_response(redirect('/'))
        response.set_cookie('user_id', str(user[0]), max_age=10000)
        return response
    return render_template('register.html')

@app.route('/login', methods= ["GET", "POST"])
def login():
    if request.method == 'POST':
        data = request.form
        password = data.get('password')
        email = data.get('email') 
        user = get_user_by_email(email)
        if user:
           if user[3] == password:
               response = make_response(redirect('/'))
               response.set_cookie('user_id', str(user[0]), max_age=10000)
               return response
           return 'неверно'
        return redirect('/')
    return render_template('login.html')


@app.route('/search_posts', methods=['POST'])
def search_posts():
    data = request.form
    search_text = data.get('search_text')
    posts = search_posts_by_text(search_text)
    return posts


if __name__ == '__main__':
    app.run(debug=True)

