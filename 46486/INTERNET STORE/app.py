from flask import Flask, render_template, request, redirect
from db import *
app = Flask(__name__)


@app.route('/')
def main():
    # 1. TODO: Получить все посты
    return render_template('main.html') # 2. TODO: передать в шаблон все посты


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = get_user_by_email(email)

        if user is None:
            add_user(name, email, password)
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
            return redirect('/profile/')     
        else:
            return render_template('login.html', message="Пароль неверный")
        
    return render_template('login.html')


@app.route('/new_post/')
def new_post():
    return render_template('new_post.html')


@app.route('/add_post/', methods=['POST'])
def add_post():
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_posts(title, content)
    return "Пост добавлен"


if __name__=='__main__':
    app.run(debug=True)