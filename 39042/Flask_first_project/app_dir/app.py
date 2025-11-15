from flask import Flask
from db import *


app = Flask(__name__)


@app.route('/')
def welcome():
    return "Hello"


if __name__  == '__main__':
    app.run()