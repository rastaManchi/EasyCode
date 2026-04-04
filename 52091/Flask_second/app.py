from flask import Flask, render_template, request
from db import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
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


if __name__ == '__main__':
    app.run()
