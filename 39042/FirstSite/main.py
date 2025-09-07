from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def welcome():
    return "<a href='https://google.com'>Кнопка</a>"


@app.route("/profile")
def profile():
    return "Профиль"


app.run()
