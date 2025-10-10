from flask import Flask, request, render_template, make_response
from models import db


app = Flask(__name__)


@app.route('/')
def welcome():
    cookies = request.cookies
    session = cookies.get("Session")
    if session:
        return render_template('index.html')
    return render_template('signintest.html')

@app.route('/signin', methods=['POST'])
def signin():
    data = request.form
    login = data.get('login')
    password = data.get('password')
    user = db.get_user(login, password)
    if user:
        response = make_response(render_template("index.html"))
        response.set_cookie("Session", user.id, 4000)
        return response
    else:
        db.create_user(login, password)
        user = db.get_user(login, password)
        response = make_response(render_template("index.html"))
        response.set_cookie("Session", user.id, 4000)
        return response
    # if login == '1234@mail.ru' and password == 'qwerty':
    #     response = make_response(render_template('index.html'))
    #     response.set_cookie('Session', 'true', 100)
    #     return response
    # else:
    #     return render_template('signin.html')
    
@app.route("/logout")
def logout():
    response = make_response(render_template('index.html'))
    response.set_cookie("Session", "Bulat", max_age=0)
    return response

app.run(host="0.0.0.0", port=80)
