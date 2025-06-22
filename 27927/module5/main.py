from flask import Flask, render_template, redirect, request, make_response, jsonify
from db import *
from test import *
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    id = request.cookies.get('id')
    if id:
        posts = get_all_posts()
        return render_template('account.html', posts=posts)
    else:
        return render_template('index.html')
    

@app.route('/verified/')
def verify():
    email = request.args.get('email')
    verify_account(email)
    user = get_user_by_email(email)
    response = make_response(redirect('/'))
    response.set_cookie('id', str(user[0]), max_age=40)
    return response
    


@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('pass')
    already = get_user_by_email(email)
    if not already:
        new_account(name, email, password)
        # check_email(email, f'Перейди по ссылке: http://127.0.0.1:5000/verified/?email={email}')
    else:
        user_pass = already[3]
        if user_pass == password:
            response = make_response(redirect('/'))
            response.set_cookie('id', str(already[0]), max_age=5400)
            return response
    return redirect('/')


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        id = int(request.cookies.get('id'))
        user = get_user_by_id(id)
        if user[4] == 1:
            users = get_all_users()
            return render_template('admin.html', data={'users': users})
        else:
            return redirect('/')
    else:
        data = request.get_json()
        event = data.get('event')
        user_id = data.get('user_id')
        if event == 'delete':
            delete_user_by_id(user_id)
        elif event == 'edit':
            pass
        return jsonify({"success": True})


@app.route('/ajax', methods=['POST', 'GET'])
def ajax():
    if request.method == 'GET':
        return render_template('ajax.html')
    else:
        data = request.get_json()
        print(data.get('name'))
        result = {
            "Ключ1": 'Значение1',
            "Ключ2": 'Значение2',
            "Ключ3": 'Значение3'
        }
        return jsonify(result)


@app.route('/add_post', methods=['POST', 'GET'])
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        add_new_post(title, content)
    return redirect('/')


app.run()
