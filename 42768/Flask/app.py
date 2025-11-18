from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def welcome():
    return '''
<h1>Привет!</h1>
<p>Если ты видишь это сообщение, значит сервер работает.</p>
<p>Держи яблоко!</p>
<img src="https://avatars.mds.yandex.net/i?id=8baaa2b8e6bb9ed857ec28a7e1f1c9e6df4d6947-5844149-images-thumbs&n=13" width="500" height="500">
'''


@app.route('/frogs')
def frogs():
    return '''
<h1>Привет!</h1>
<p>Если ты видишь это сообщение, значит сервер работает.</p>
<p>Держи яблоко!</p>
<img src="https://avatars.mds.yandex.net/i?id=8baaa2b8e6bb9ed857ec28a7e1f1c9e6df4d6947-5844149-images-thumbs&n=13" width="500" height="500">
'''


if __name__ == "__main__":
    app.run()
    
