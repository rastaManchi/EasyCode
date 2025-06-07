from flask import Flask, render_template, redirect, request, make_response
from db import *
from test import *

app = Flask(__name__)

@app.route('/')
def welcome():
    id = request.cookies.get('id')
    if id:
        return render_template('account.html')
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
        check_email(email, f'Перейди по ссылке: http://127.0.0.1:5000/verified/?email={email}')
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
        delete_id = request.form.get('delete_id')
        edit_id = request.form.get('edit_id')
        if delete_id:
            delete_user_by_id(delete_id)
        elif edit_id:
            pass
        return redirect('/admin')


app.run()
