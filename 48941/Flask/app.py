from flask import Flask, render_template


app = Flask(__name__) # __name__ = '__main__'



# http://127.0.0.1:5000 = '/'
# http://127.0.0.1:5000/login/ = '/login/'
@app.route('/')
def welcome():
    return render_template('index.html', data={
        'title': 'Привет!',
        'paragraph': 'Если ты видишь это сообщение, значит сервер работает.',
        'img': 'https://zelensad.com/upload/iblock/490/490d38e33c65dfe7f1df16c83a446e45.png'
    })


@app.route('/frogs/')
def frogs():
    return render_template('index.html', data={
        'title': 'Лягухи!',
        'paragraph': 'общеупотребительное название группы животных из отряда бесхвостых земноводных. В широком смысле термин «лягушка»относится ко всем представителям отряда бесхвостых, в узком — к представителям семейства настоящих лягушек',
        'img': 'https://stihi.ru/pics/2012/12/13/4458.jpg'
    })


@app.route('/hobby/')
def hobby():
    return render_template('hobby.html')


app.run()