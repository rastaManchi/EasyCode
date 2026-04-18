from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   session,
                   g,
                   jsonify)
from db import *
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
import secrets
from functools import wraps

import traceback
import logging
from logging.handlers import RotatingFileHandler


if not os.path.exists('logs'):
    os.mkdir('logs')


format = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
file_handler = RotatingFileHandler(
    'logs/blog.log',
    maxBytes=10240,
    backupCount=10
)
file_handler.setFormatter(format)
file_handler.setLevel(logging.INFO)


def session_repair(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('auth_token')
        g.user_id = None
        if token:
            user_id = validate_token(token)
            if user_id:
                user = get_user_by_id(user_id)
                session['user_id'] = user[0]
                session['username'] = user[1]
                g.user_id = user[0]
        
        g.username = session.get('username')
        result = func(*args, **kwargs)
        return result
    return wrapper


def check_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if g.user_id:
            user = get_user_by_id(g.user_id)
            if user[4]:
                result = func(*args, **kwargs)
                return result
        return redirect('/')
    return wrapper


load_dotenv()


def send_mail(to_email, username):
    from_email = os.getenv("MAIL_LOGIN")
    password = os.getenv("MAIL_PASSWORD")
    if not from_email or not password:
        print("ОШИБКА: Не найдены EMAIL_USER или EMAIL_PASSWORD в .env файле!")
        exit()
    
    subject = "Добро пожаловать в наш блог!"
    body = f"Привет, {username}\nСпасибо за регистрацию!"
        
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print("Ошибка аутентификации - неверный логин или пароль")
    except Exception as e:
        print(f"Ошибка подключения: {e}")


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/')
@session_repair
def main():
    page = request.args.get('page', 1, type=int)
    limit = 2
    offset = (page - 1) * limit
    posts_count = get_posts_count()
    pages = (posts_count + limit - 1) // limit
    posts = get_posts_by_offset(limit, offset)
    return render_template('main.html',
                           username=g.username,
                           posts=posts,
                           page=page,
                           pages=pages)
  
    
@app.route('/load_more')
def load_more():
    page = request.args.get('page', 1, type=int)
    limit = 2
    offset = (page - 1) * limit
    posts = get_posts_by_offset(limit, offset)
    result_posts = []
    for post in posts:
        result_posts.append({
            'id': post[0],
            'title': post[1],
            'content': post[2],
            'author': post[3]
        })
    return jsonify(result_posts)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = get_user_by_email(email)

        if user is None:
            add_user(name, email, password)
            send_mail(email, name)
            return redirect('/profile/')
        else:
            print('Такой пользователь уже есть')

    return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = get_user_by_email(email)
        if user is None:
            return render_template('login.html', message="Нет такой почты")
        if user[3] == password:
            print('Вход выполнен')
            token = create_token(user[0])
            session['user_id'] = user[0]
            session['username'] = user[1]
            result = redirect('/profile/')
            result.set_cookie('auth_token',
                              token,
                              60 * 10)
            return result   
        else:
            return render_template('login.html', message="Пароль неверный")
    return render_template('login.html')


@app.route('/search/')
@session_repair
def search():
    search_text = request.args.get('search_text', '')
    posts = get_posts_by_search(search_text)
    return render_template('main.html', username=g.username, posts=posts)
    

@app.route('/new_post/')
def new_post():
    return render_template('new_post.html')


@app.route('/add_post/', methods=['POST'])
@session_repair
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_posts(title, content, g.user_id)
    return "Пост добавлен"


@app.route('/user/<int:user_id>')
def user(user_id):
    user = get_user_by_id(user_id)
    if user:
        posts = get_posts_by_user_id(user_id)
        return render_template('profile.html', posts=posts, user=user)
    return "Пользователь не найден!", 404


@app.route('/admin')
@session_repair
@check_admin
def admin():
    zeroposts = get_posts_by_status(0)
    approvedposts = get_posts_by_status(1)
    disapprovedposts = get_posts_by_status(2)
    return render_template('admin.html',
                           zeroposts=zeroposts,
                           approvedposts=approvedposts,
                           disapprovedposts=disapprovedposts)
    

@app.route('/approve/<int:post_id>')
@session_repair
@check_admin
def approve(post_id):
    set_post_status(post_id, 1)
    return redirect('/admin')


@app.route('/disapprove/<int:post_id>')
@session_repair
@check_admin
def disapprove(post_id):
    set_post_status(post_id, 2)
    return redirect('/admin')


@app.route('/delete/<int:post_id>')
@session_repair
@check_admin
def delete(post_id):
    delete_post(post_id)
    return redirect('/admin')


@app.route('/error500')
def test_error500():
    10/0
    return 'OK'


@app.errorhandler(404)
def error_404(error_text):
    app.logger.error(error_text)
    return render_template('404.html'), 404


@app.errorhandler(Exception)
def handle_all_errors(error_text):
    if app.debug:
        error_traceback = traceback.format_exc()
        return render_template('error_traceback.html',
                               error_type=type(error_text).__name__,
                               error_traceback = error_traceback)
    else:
        app.logger.error(error_text)
        return render_template('500.html', error_text=error_text), 500


if __name__=='__main__':
    app.run(debug=True)