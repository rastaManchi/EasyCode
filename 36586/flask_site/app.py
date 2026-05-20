from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def home():
    name = 'Булат'
    return render_template('home.html', name=name)

app.run()
