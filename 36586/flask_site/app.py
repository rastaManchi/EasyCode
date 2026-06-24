from flask import Flask, render_template, request, session, jsonify, redirect
from db import (get_user_by_email, 
                create_user,
                create_auth_token,
                validate_auth_token,
                get_user_by_id,
                create_api_token,
                validate_api_token)
import secrets
from functools import wraps


def check_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_token = request.cookies.get('auth_token')
        if auth_token:
            user_id = validate_auth_token(auth_token)
            if user_id:
                user = get_user_by_id(user_id)
                session['user_id'] = user[0]
                session['username'] = user[1]
        result = func(*args, **kwargs)
        return result
    return wrapper


def check_api(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_token = request.headers.get('Authorization')
        if not api_token:
            return jsonify({
                'status': 'error',
                'message': 'Токен не указан'
            }), 401
        if not validate_api_token(api_token):
            return jsonify({
                'status': 'error',
                'message': 'Токен не действителен'
            }), 401
        result = func(*args, **kwargs)
        return result
    return wrapper


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
@check_session
def home():
    name = session.get('username', 'Аноним')
    return render_template('home.html', name=name)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        user = get_user_by_email(email)
        if user:
            if password == user[3]:
                session['user_id'] = user[0]
                session['username'] = user[1]
                token = create_auth_token(user[0])
                response = redirect('/')
                response.set_cookie('auth_token', token, 600)
                return response
        return 'Неверные данные'
    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user = get_user_by_email(email)
        if not user:
            create_user(username, email, password)
            return "Пользователь создан"
    return render_template('signup.html')


@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    email = data.get('login')
    password = data.get('password')
    user = get_user_by_email(email)
    if user:
        if password == user[3]:
            token = create_api_token(user[0])
            return jsonify({
                'status': 'success',
                'token': token
            })
    return jsonify({
        'status': 'failed'
    })


@app.route('/api/info')
@check_api
def info():
    return jsonify({
        'status': 'success',
        'info': 'OK'
    })


app.run()
