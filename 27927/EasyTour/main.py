from flask import Flask, render_template, request, redirect
from helpers import *
import random

app = Flask(__name__)



@app.route('/')
def main():
    tours = get_all_tours()
    print(tours)
    return render_template('index.html', data={'tours': random.sample(tours, 8)})


app.run(debug=True)