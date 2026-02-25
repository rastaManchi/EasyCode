from flask import Flask, render_template, request, redirect
from db import *


app = Flask(__name__)


#http://127.0.0.1:5000/test
@app.route('/test')
def test():
    return render_template('test.html')


#http://127.0.0.1:5000/
@app.route('/')
def home():
    posts = get_all_posts()
    users = get_all_users()
    return render_template('main.html', posts=posts, users=users)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/user/<int:user_id>')
def get_user_profile(user_id):
    user = get_user_by_id(user_id)
    posts = get_posts_by_user_id(user_id)
    if user:
        return render_template('user_page.html',
                            user=user,
                            posts=posts)
    return "Пользователь не найден", 404


@app.route('/new_post')
def new_post():
    return render_template('new_post.html')


@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_new_post(title, content)
    return redirect('/')


#http://127.0.0.1:5000/login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        user = get_user_by_email(email)
        if user:
            if user[3] == password:
                return "Successed"
            return "Wrong password"
        return "User not found"
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
