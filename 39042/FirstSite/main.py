from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def welcome():
    return "Привет"


@app.route("/profile")
def profile():
    return "Профиль"


app.run()
