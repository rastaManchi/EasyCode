from flask import Flask, render_template, request, redirect
from db import *


app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
