from flask import Flask


app = Flask(__name__)


# http://127.0.0.1:5000/
@app.route('/')
def home():
    return '''
<h1>Привет!</h1>
<p>Если ты видишь это сообщение, значит сервер работает.</p>
<p>Держи яблоко!</p>
<img src="https://clck.ru/34RZGh" width="500" height="500">
'''



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
