from flask import Flask


app = Flask(__name__) # __name__ = '__main__'



# http://127.0.0.1:5000 = '/'
# http://127.0.0.1:5000/login/ = '/login/'
@app.route('/')
def welcome():
    return '''
<h1>Привет!</h1>
<p>Если ты видишь это сообщение, значит сервер работает.</p>
<p>Держи яблоко!</p>
<img src="https://zelensad.com/upload/iblock/490/490d38e33c65dfe7f1df16c83a446e45.png" width="500" height="500">
'''

@app.route('/frogs/')
def frogs():
    return '''
<h1>Лягухи</h1>
<p>общеупотребительное название группы животных из отряда бесхвостых земноводных. В широком смысле термин «лягушка» относится ко всем представителям отряда бесхвостых, в узком — к представителям семейства настоящих лягушек</p>
<img src="https://stihi.ru/pics/2012/12/13/4458.jpg" width="500" height="500">
'''


app.run()