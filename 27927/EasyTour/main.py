from flask import Flask, render_template, request, redirect, make_response
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
        history = []
        tour = get_tour_by_id(tour_id)
        if request.cookies.get('id') is not None:
            old_cookies = request.cookies.get('id')
            print(old_cookies)
            cookies_massive = old_cookies.split(';')
            if str(tour_id) not in cookies_massive:
                cookies_massive.append(str(tour_id))
            for id in cookies_massive:
                history_tour = get_tour_by_id(int(id))
                history.append(history_tour)
            response = make_response(render_template('tour.html', data={'tour': tour, 'history': history}))
            response.set_cookie('id', ';'.join(cookies_massive), max_age=40)
            return response
        else:
            response = make_response(render_template('tour.html', data={'tour': tour, 'history': history}))
            response.set_cookie('id', str(tour_id), max_age=40)
            return response
    add_like(tour_id)
    return redirect(f'/tour/{tour_id}')


@app.route('/check_cookies/')
def check_cookies():

    if request.cookies.get('a') is not None:
        return render_template('cookies.html')
    else:
        response = make_response(render_template('cookies.html'))
        response.set_cookie('a', 'b', max_age=40)
        return response


app.run(debug=True)


