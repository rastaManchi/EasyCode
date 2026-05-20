from flask import Flask, render_template, request, redirect
from db import *


app = Flask(__name__)


@app.route('/')
def home():
    all_posts = get_all_posts()
    return render_template('home.html', posts=all_posts)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        user = get_user_by_email(email)
        if user and user[3] == password:
            return 'Доступ разрешен'
        return 'Неверные данные'
    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        user_name = data.get('name')
        user_email = data.get('email')
        user_password = data.get('password')
        if user_name and user_email and user_password:
            user = get_user_by_email(user_email)
            if not user:
                create_user(user_name, user_email, user_password)
                return "Пользователь создан"
    return render_template('signup.html')


@app.route('/new_post')
def new_post():
    return render_template('add_post.html')


@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    create_post(title, content)
    return redirect('/')


if __name__ == '__main__':
    app.run()
