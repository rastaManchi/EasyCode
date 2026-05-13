from flask import Flask, render_template, redirect, request, make_response, session, jsonify
from help import *
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
import secrets


import logging
from logging.handlers import RotatingFileHandler

from functools import wraps


load_dotenv()
from_email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASSWORD")


cached = {}


def send_mail(email_to):
    if not from_email or not password:
        print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
        return False
    subject = "Добро пожаловать!"
    body = """
Добрый день!
Спасибо, что выбрали нас!

Команда ... <3
    """
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = email_to
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
        return True
    except smtplib.SMTPAuthenticationError:
        print("Ошибка аутентификации - неверный логин или пароль")
    except Exception as e:
        print(f"Ошибка подключения: {e}")
    return False


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


if not os.path.exists('logs'):
    os.mkdir('logs')
    
file_handler = RotatingFileHandler('logs/app.log',
                                   maxBytes=10240,
                                   backupCount=10,
                                   encoding='utf-8')
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Test')
app.logger.warning('Test')
app.logger.error('Test')


def check_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        if user_id:
            user = get_user_by_id(user_id)
            if user[4]:
                result = func(*args, **kwargs)
                return result
        return redirect('/'), 403
    return wrapper


def api_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_token = request.headers.get('Authorization')
        if not api_token:
            return jsonify({
                'status': 40101,
                'msg': 'Authorization не указан'
            }), 401
        if not validate_api_token(api_token):
            return jsonify({
                'status': 40102,
                'msg': 'Authorization не верный'
            }), 401
        result = func(*args, **kwargs)
        add_api_request(api_token)
        return result
    return wrapper


@app.route('/admin')
@check_admin
def admin():
    zeroposts = get_posts_by_status(0)
    approvedposts = get_posts_by_status(1)
    disapprovedposts = get_posts_by_status(2)
    return render_template('admin.html',
                           zeroposts=zeroposts,
                           approvedposts=approvedposts,
                           disapprovedposts=disapprovedposts)
    
    
@app.route('/approve')
@check_admin
def approve():
    id = request.args.get('id')
    set_post_status(1, id)
    return redirect('/admin')


@app.route('/disapprove')
@check_admin
def disapprove():
    id = request.args.get('id')
    set_post_status(2, id)
    return redirect('/admin')


@app.route('/')
def main():
    token = request.cookies.get('auth_token')
    if token:
        user_id = validate_token(token)
        if user_id:
            user = get_user_by_id(user_id)
            session['user_id'] = user[0]
            session['username'] = user[1]
    username = None
    if 'username' in session:
        username = session['username']
        
    current_page = int(request.args.get('page', 1))
    posts_per_page = 3
    offset = (current_page - 1) * posts_per_page
    posts_count = get_posts_count()
    max_page = posts_count // posts_per_page
    posts = get_all_posts_by_page(posts_per_page, offset)
    users = get_all_users()
    return render_template('main.html',
                           posts = posts,
                           users=users,
                           username=username,
                           current_page=current_page,
                           max_page = max_page)


@app.route('/profile/<int:user_id>')
def profile(user_id):
    posts = get_posts_by_user_id(user_id)
    return render_template('profile.html', posts=posts)


@app.route('/new_post')
def new_post():   
    return render_template('new_post.html') 


@app.route('/add_post', methods = ["POST"])
def post():
    user_id = None
    if 'user_id' in session:
        user_id = session['user_id']
        data = request.form
        title = data.get('title')
        content = data.get('content')
        add_new_post(title, content, user_id)
        return redirect('/')
    return "Вы не авторизованы", 401


@app.route('/admin/post/edit/<int:post_id>', methods=['GET', 'POST'])
@check_admin
def edit_post(post_id):
    post = get_post_by_id(post_id)
    if request.method == 'POST':
        data = request.form
        new_title = data.get('title')
        new_content = data.get('content')
        update_post(post_id, new_title, new_content)
        return redirect('/')
    return render_template('edit_post.html',
                           title=post[1],
                           content=post[2])


@app.route('/register', methods= ["GET", "POST"])
def register():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')
        add_user(name, email, password)
        user = get_user_by_email(email)
        send_mail(email)
        response = make_response(redirect('/'))
        session['user_id'] = user[0]
        session['username'] = user[1]
        return response
    return render_template('register.html')


@app.route('/login', methods= ["GET", "POST"])
def login():
    if request.method == 'POST':
        data = request.form
        password = data.get('password')
        email = data.get('email') 
        user = get_user_by_email(email)
        if user:
           if user[3] == password:
               response = make_response(redirect('/'))
               token = create_token(user[0], True)
               response.set_cookie('auth_token', token, max_age=60 * 10)
               session['user_id'] = user[0]
               session['username'] = user[1]
               return response
           return 'неверно'
        return redirect('/')
    return render_template('login.html')


@app.route('/search_posts', methods=['POST'])
def search_posts():
    data = request.form
    search_text = data.get('search_text')
    posts = search_posts_by_text(search_text)
    return posts


@app.route('/docs')
def docs():
    return render_template('api_docs.html')


@app.route('/api/v1/search_posts')
@api_check
def api_search_posts():
    q = request.args.get('q')
    
    if f"api_search_q{q}" in cached and time.time() - cached[f"api_search_q{q}"].get('last_updated') < 20:
        print(cached)
        return jsonify(cached[f"api_search_q{q}"])
    
    posts = search_posts_by_text(q)
    result = []
    for post in posts:
        result.append({
            'id': post[0],
            'title': post[1],
            'content': post[2]
        })
    cached[f"api_search_q{q}"] = {
            'status': 2000,
            'msg': 'Кэшировано',
            'data': result,
            'last_updated': time.time()
        }
    return jsonify({
            'status': 2000,
            'msg': 'Успешно',
            'data': result
        })


@app.route('/api/v1/login' , methods=['POST'])
def api_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = get_user_by_email(email)
    if user and user[3] == password:
        token = create_api_token(user[0])
        return jsonify({
            'status': 2000,
            'msg': 'Успешно',
            'token': token
        })
    return jsonify({
                'status': 40103,
                'msg': 'Данные неверные'
            }), 401
        


@app.route('/api/v1/posts')
@api_check
def api_posts():
    posts = get_all_posts()
    return jsonify({
        'status': 2000,
        'msg': 'Hello',
        'data': posts
    })


@app.errorhandler(404)
def error_404(error):
    app.logger.error(error)
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)

