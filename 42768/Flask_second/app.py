from flask import Flask, render_template, request, redirect
from db import *


app = Flask(__name__)


@app.route('/')
def home():
    all_posts = get_all_posts()
    all_users = get_all_users()
    # 1. TODO: В main.html отображать актуальные данные постов
    # 2. TODO: Добавить рядом с каждым постом имя автора
    return render_template('main.html', all_users=all_users, all_posts=all_posts)


# 3. TODO: Создайте страницу "Все пользователи", 
    # где будет отображаться список всех зарегистрированных пользователей с указанием количества их постов. 
    # Для этого:
        # Создайте новый маршрут /users
        # Напишите SQL-запрос(в db.py), который считает количество постов для каждого пользователя
        # Создайте шаблон для отображения этой информации (в templates users.html)
        
        
# 4. TODO: Реализуйте возможность редактирования и удаления постов. 
    # Добавьте на страницу пользователя кнопки "Редактировать" и "Удалить" для каждого его поста. 
    # Для этого:
        # Создайте новые маршруты /post/<int:post_id>/edit и /post/<int:post_id>/delete
        # Добавьте проверку, что только автор поста может его редактировать и удалять
        # Создайте формы для редактирования поста


#http://127.0.0.1:5000/user/1
@app.route('/user/<int:user_id>')
def user(user_id):
    print(type(user_id))
    user = get_user_by_id(user_id)
    user_posts = get_posts_by_user(user_id)
    if user:
        return render_template('user_template.html', user=user, user_posts=user_posts)
    return f"Пользователь не найден", 404


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        user = get_user_by_email(email)
        if user:
            user_pass = user[0][3]
            if user_pass == password:
                return "Успешно"
            return "Неверный пароль"
        return "Неверная почта"
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        add_user(name, email, password)
        return "Успешно"
    return render_template("register.html")


@app.route('/post')
def post():
    return render_template('new_posts.html')


@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_post_to_db(title, content, 1)
    return redirect('/')


app.run()