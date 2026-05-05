from flask import Flask, render_template, request
from db import *


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signin')
def signin():
    return render_template('signin.html')


@app.route('/signup')
def signup():
    data = request.args
    user_name = data.get('name')
    user_email = data.get('email')
    user_password = data.get('password')
    if user_name and user_email and user_password:
        user = get_user_by_email(user_email)
        if not user:
            create_user(user_name, user_email, user_password)
            return "Пользователь создан"
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
