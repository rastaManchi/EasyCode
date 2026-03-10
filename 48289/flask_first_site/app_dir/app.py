from flask import Flask, render_template, request


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


@app.route('/methods')
def methods():
    data = request.args
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    return render_template('methods.html')


@app.route('/postmethods', methods=['GET', 'POST'])
def postmethods():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')
        return f"{username} - {password}"
    return render_template('methods_post.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
