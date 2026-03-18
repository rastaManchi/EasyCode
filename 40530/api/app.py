from flask import Flask, request, g, session, render_template, jsonify
from functools import wraps


AUTH_TOKEN = 'SADJFGSKLVSDKKFGCASZXKC'
ADMIN_AUTH_TOKEN = 'sdfsdkfsdgksdifgsjkfsd'


def check_api_token(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        g.bulat = 'Привет, Булат!'
        auth_token = request.headers.get('Authorization', 'Ключа нет')
        if auth_token != AUTH_TOKEN:
            return jsonify({'status': 'failed'}), 401
        return function(*args, **kwargs)
    return wrapper


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/home')
@check_api_token
def api_home():
    data = {
        'name': 'Булат',
        'email': 'bulat-zakirov.01@mail.ru'
    }
    return jsonify(data)


@app.route('/api/test')
@check_api_token
def api_test():
    return jsonify({'status': g.bulat})


app.run()
