from flask import Flask, render_template, request
from second import *

app = Flask(__name__)

@app.route("/")
def welcome():
    return '''<a href="/frogs">Лягушки</a>'''


app.run()