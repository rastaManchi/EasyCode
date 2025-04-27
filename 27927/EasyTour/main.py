from flask import Flask, render_template, request, redirect
import sqlite3
from helpers import *
import random

app = Flask(__name__)

@app.route('/')
def main():
    if len(request.args) == 0:
        tours = random.sample(list(get_tour_covers()), 8)
        return render_template('index.html', data={'tours': tours, 'tour_heading': f'Лучшие туры'})
    
    elif request.args.get('category'):
        category = request.args.get('category')
        result = get_tours_by_category(category)
        return render_template('index.html', data={'tours': result, 'tour_heading': f'Результаты по запросу: {category}'})

    keyword = request.args.get('keyword')
    minprice = int(request.args.get('minprice'))
    maxprice = int(request.args.get('maxprice'))
    
    result = get_tours_with_keywords(minprice, maxprice, keyword)
    
    if len(result) <= 8:
        return render_template('index.html', data={'tours': result, 'tour_heading': f'Результаты по запросу: {keyword}'})
        
    return render_template('index.html', data={'tours': random.sample(tours, 8), 'tour_heading': f'Результаты по запросу: {keyword}'})


app.run(debug=True)


