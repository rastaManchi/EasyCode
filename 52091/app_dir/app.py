from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    data = request.args
    arg1 = data.get('username')
    return arg1


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('email')
        password = data.get('password')
        return f"{email} - {password}"
    return render_template('login.html')


@app.route('/register')
def register():
    return "200"


if __name__ == "__main__":  
    app.run()
else:
    print('app.py не файл запуска!')