from flask import Flask, render_template, request, redirect, make_response
from db import *
import requests
import json


def get_weather(city_name):
    API_KEY = "3140cf48db6a89dd9eb2dc1338ae400d"
    r = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={API_KEY}")
    data = json.loads(r.content)
    lat = data[0]['lat']
    lon = data[0]['lon']

    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
    data = json.loads(r.content)
    temp = data['main']['temp'] - 273

    return temp


app = Flask(__name__)


@app.route('/api/', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        city = request.form.get("city")
        temp = get_weather(city)
        return render_template('api.html', last_result=temp)
    return render_template('api.html')


@app.route('/')
def welcome():
    posts = get_all_posts()
    is_admin = None
    user_id = request.cookies.get('Session')
    if user_id:
        user = get_user_by_id(user_id)
        is_admin = user[4]
    return render_template('main.html', posts=posts, is_admin=is_admin)


@app.route('/delete/')
def delete_post():
    user_id = request.cookies.get('Session')
    if user_id == '2':
        data = request.args
        print(data)
        post_id = int(data.get('post_id'))
        delete_post_by_id(post_id)
        return redirect('/')
    

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = get_user_by_email(email)
        if user is None:
            add_user(name, email, password)
            user = get_user_by_email(email)
            response = make_response(redirect('/profile/'))
            response.set_cookie('Session', str(user[0]), max_age=3600)
            return response
        else:
            print('Такой пользователь уже есть!')
    return render_template('signup.html')


@app.route('/signin/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = get_user_by_email(email)
        
        if user is None:
            return render_template('signin.html', message='Нет такой почты!')
        
        if user[3] == password:
            print('Вход разрешен')
            response = make_response(redirect('/profile/'))
            response.set_cookie('Session', str(user[0]), max_age=3600)
            return response
        else:
            return render_template('signin.html', message='Пароль неверный')
    return render_template('signin.html')


@app.route('/profile/')
def profile():
    user_id = request.cookies.get('Session')
    if user_id:
        user = get_user_by_id(int(user_id))
        response = {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "password": user[3]
        }
        return render_template('profile.html', data=response)
    return 'Вы не авторизованы'


@app.route('/add_post/', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        user_id = request.cookies.get('Session')
        if user_id:
            title = request.form.get('title')
            content = request.form.get('content')
            add_new_post(title, content, user_id)
            return redirect('/')
    return render_template('add_post.html')


@app.route('/search/', methods=['POST'])
def search():
    data = request.form
    txt = data.get('txt')
    posts = search_post(txt)
    return posts


@app.route('/admin')
def admin():
    user_id = request.cookies.get('Session')
    is_admin = 0
    if user_id:
        user = get_user_by_id(user_id)
        is_admin = user[4]
    if is_admin:
        posts = get_notchecked_posts()
        data = []
        for post in posts:
            author = get_user_by_id(post[3])
            data.append(
                {
                    'title': post[1],
                    'content': post[2],
                    'created_at': post[5],
                    'author_name': author[1]
                }
            )
        return render_template('admin.html', posts=data)
    return redirect('/')


@app.route('/check/')
def check():
    user_id = request.cookies.get('Session')
    is_admin = 0
    if user_id:
        user = get_user_by_id(user_id)
        is_admin = user[4]
    if is_admin:
        data = request.args
        post_id = data.get('id')
        status = data.get('approve')
        change_post_status(post_id, status)
        return redirect('/admin')
    return redirect('/')


if __name__  == '__main__':
    app.run(host='0.0.0.0', port='80')