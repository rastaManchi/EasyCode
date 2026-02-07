from flask import Flask, render_template, request, redirect
from db import *


app = Flask(__name__)


@app.route('/')
def home():
    # 1. в db.py
    # 2. TODO: получить все посты и сохранить в переменную 
    # 3. TODO: передать вместе с шаблоном посты
    # 4. TODO: По желанию. В main.html отображать актуальные данные постов
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        user = get_user_by_email(email)
        if user:
            user_pass = user[0][3]
            if user_pass == password:
                return "Успешно"
            return "Неверный пароль"
        return "Неверная почта"
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        add_user(name, email, password)
        return "Успешно"
    return render_template("register.html")


@app.route('/post')
def post():
    return render_template('new_posts.html')


@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_post_to_db(title, content)
    return redirect('/')


app.run()