from flask import Flask, request, render_template, make_response


app = Flask(__name__)


@app.route('/')
def welcome():
    cookies = request.cookies
    session = cookies.get("Session")
    if session:
        return "Ты авторизован!"
    return render_template('index.html')


@app.route('/login')
def login():
    response = make_response(render_template('index.html'))
    response.set_cookie("Session", "Bulat", max_age=30)
    return response


@app.route("/logout")
def logout():
    response = make_response(render_template('index.html'))
    response.set_cookie("Session", "Bulat", max_age=0)
    return response


app.run(host="0.0.0.0", port=80)
