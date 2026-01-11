from flask import Flask, request, render_template, redirect, make_response
from db import *


app = Flask(__name__)


@app.route('/')
def welcome():
    posts = get_posts()
    return render_template('main.html', posts=posts)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data['email']
        password = data.get('password')
        
        user = get_user_by_email(email)
        if user:
            print('Такой пользователь уже существует.')
        else:
            add_user(name, email, password)
            user = get_user_by_email(email)
            response = make_response(redirect('/profile/'))
            response.set_cookie('session', str(user[0][0]), 60)
            return response
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
                response = make_response(redirect('/profile/'))
                response.set_cookie('session', str(user[0][0]), 60)
                return response
            else:
                print('Пароль неверный')
        else:
            print('Пользователя не существует')
    return render_template('login.html')


@app.route('/add_post/', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        data = request.form
        title = data.get('title')
        content = data.get('content')
        add_post_in_db(title, content)
        return redirect('/profile/')
    return render_template('add_post.html')


if __name__ == '__main__':
    app.run()