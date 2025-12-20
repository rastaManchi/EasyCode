from flask import Flask, render_template


app = Flask(__name__) # __name__ = '__main__'



# http://127.0.0.1:5000 = '/'
# http://127.0.0.1:5000/login/ = '/login/'
@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/frogs/')
def frogs():
    return render_template('frogs.html')


@app.route('/hobby/')
def hobby():
    return render_template('hobby.html')


app.run()