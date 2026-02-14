from flask import Flask, render_template, request
from db import *


app = Flask(__name__)


#http://127.0.0.1:5000/test
@app.route('/test')
def test():
    return render_template('test.html')


#http://127.0.0.1:5000/
@app.route('/')
def home():
    return render_template('main.html')


#http://127.0.0.1:5000/login
# 1. TODO: Разрешить метод POST
@app.route('/login')
def login():
    # 2. TODO: Проверить метод
        # 3. TODO: Получить данные от пользователя
        # 4. TODO: Проверить данные
        # 5. TODO: Вернуть Success или Failed 
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
            return render_template('profile.html')
    return render_template('register.html')


app.run()
