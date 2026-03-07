from flask import Flask, render_template


app = Flask(__name__)


# http://127.0.0.1:5000/
# https://vk.com/
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/frogs')
def frogs():
    return render_template('animal.html', title="Лягушки")


@app.route('/snails')
def snails():
    return render_template('animal.html', title="Улитки")


@app.route('/dynos')
def dynos():
    return render_template('animal.html', title="Динозавры")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
