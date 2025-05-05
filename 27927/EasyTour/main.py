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


# http://127.0.0.1:port/tour/?id=2
@app.route('/tour/', methods=['POST'])
def tour():
    tour_id = int(request.args.get('id'))
    tour = get_tour_by_id(tour_id)
    return render_template('tour.html', data={'tour': tour}) 


# http://127.0.0.1:port/tour/2
@app.route('/tour/<int:tour_id>', methods=['GET', 'POST'])
def tour2(tour_id):
    if request.method == 'GET':
        tour = get_tour_by_id(tour_id)
        return render_template('tour.html', data={'tour': tour}) 
    add_like(tour_id)
    return redirect(f'/tour/{tour_id}')

app.run(debug=True)


