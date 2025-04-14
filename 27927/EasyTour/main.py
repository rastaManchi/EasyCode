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
    
    keyword = request.args.get('keyword')
    minprice = int(request.args.get('minprice'))
    maxprice = int(request.args.get('maxprice'))
    tours = get_all_tours()
    price_fit = []
    for tour in tours:
        if maxprice >= tour[3] >= minprice:
            price_fit.append(tour)
    result = []
    for tour in price_fit:
        flag = False
        # Ищем только среди названия, описания и страны - индексы этих полей это 1, 2 и 5
        for i in 1, 2, 5:
            if keyword.lower() in tour[i].lower():
                flag = True
                break

        if flag:
            result.append(tour)
    
    if len(result) <= 8:
        return render_template('index.html', data={'tours': result, 'tour_heading': f'Результаты по запросу: {keyword}'})
        
    return render_template('index.html', data={'tours': random.sample(tours, 8), 'tour_heading': f'Результаты по запросу: {keyword}'})


app.run(debug=True)