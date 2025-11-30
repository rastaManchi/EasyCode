from flask import Flask, render_template, request, redirect
from db import *


app = Flask(__name__)


@app.route('/')
def welcome():
    posts = get_all_posts()
    return render_template('main.html', posts=posts)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = get_user_by_email(email)
        if user is None:
            add_user(name, email, password)
            return redirect('/profile/')
        else:
            print('Такой пользователь уже есть!')
    return render_template('signup.html')


@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = get_user_by_email(email)
        
        if user is None:
            return render_template('signin.html', message='Нет такой почты!')
        
        if user[3] == password:
            print('Вход разрешен')
            return redirect('/profile/')
        else:
            return render_template('signin.html', message='Пароль неверный')
    return render_template('signin.html')


@app.route('/profile/')
def profile():
    user = get_user_by_id(2)
    response = {
        "id": user[0],
        "name": user[1],
        "email": user[2],
        "password": user[3]
    }
    return render_template('profile.html', data=response)


@app.route('/add_post/', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        add_new_post(title, content)
        return redirect('/')
    return render_template('add_post.html')


if __name__  == '__main__':
    app.run(host='0.0.0.0', port='80')