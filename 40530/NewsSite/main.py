from flask import Flask, request, render_template, redirect
from db import *


app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('main.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        
        user = get_user_by_email(email)
        if user:
            print('Такой пользователь уже существует.')
        else:
            add_user(name, email, password)
            return redirect('/profile/')
    return render_template('register.html')


@app.route('/profile/')
def profile():
    return render_template('profile.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        
        user = get_user_by_email(email)
        if user:
            if password == user[0][3]:
                return redirect('/profile/')
            else:
                print('Пароль неверный')
        else:
            print('Пользователя не существует')
    return render_template('login.html')


@app.route('/add_post/')
def add_post():
    return render_template('add_post.html')


if __name__ == '__main__':
    app.run()