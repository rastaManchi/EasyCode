from flask import Flask, render_template, redirect, request, make_response
from help import *

app = Flask(__name__)

@app.route('/')
def main():
    user_id = request.cookies.get('user_id') 
    user = get_user_by_id(user_id) 
    posts = get_all_posts()
    # 7. TODO: Получить всех пользователей
    # 8. TODO: Передать пользователей в шаблон
    return render_template('main.html', posts = posts)

@app.route('/profile')
def profile():
    # 2. TODO: Получал все посты пользователя
    # 3. TODO: Передать посты в шаблон
    return render_template('profile.html')

@app.route('/new_post')
def new_post():   
    return render_template('new_post.html') 

@app.route('/add_post', methods = ["POST"])
def post():
    user_id = request.cookies.get('user_id') 
    data = request.form
    title = data.get('title')
    content = data.get('content')
    add_new_post(title, content, user_id)
    return redirect('/')

@app.route('/register', methods= ["GET", "POST"])
def register():
    if request.method == 'POST':
        data = request.form
        name = data.get('name')
        password = data.get('password')
        email = data.get('email')
        add_user(name, email, password)
        user = get_user_by_email(email)
        response = make_response(redirect('/'))
        response.set_cookie('user_id', str(user[0]), max_age=10000)
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
               response.set_cookie('user_id', str(user[0]), max_age=10000)
               return response
           return 'неверно'
        return redirect('/')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

