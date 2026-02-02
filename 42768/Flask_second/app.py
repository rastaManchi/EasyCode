from flask import Flask, render_template, request
from db import *


app = Flask(__name__)


@app.route('/')
def home():
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


app.run()