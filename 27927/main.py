from flask import Flask, render_template
from flask import request

app = Flask(__name__)

course = {
   'EUR': 77,
   'USD': 63,
   'UZS': 0.00692,
   'GBP': 98,
}

@app.route('/frogs/')
def frogs():
    return render_template('index.html', data={
        "title": "Лягушки",
        "description": "Лягушки — общеупотребительное название группы животных из отряда бесхвостых земноводных. В широком смысле термин «лягушка» относится ко всем представителям отряда бесхвостых. В узком смысле это название применяется по отношению к представителям семейства настоящих лягушек. Личинки лягушек называются головастиками.",
        "img1": "https://clck.ru/34RZLn",
        "img2": "https://clck.ru/34RZM8"
    })


@app.route('/snails/')
def snails():
    return render_template('index.html', data={
        "title": "Улитки",
        "description": "Ули́тки — общеупотребительное название брюхоногих моллюсков (лат. Gastropoda), обладающих наружной раковиной.",
        "img1": "https://clck.ru/34RZMp",
        "img2": "https://clck.ru/34RZNG"
    })


@app.route('/dynos/')
def dynos():
    return render_template('index.html', data={
        "title": "Динозавры",
        "description": "Динозавры – это рептилии, принадлежащие к подклассу архозавров. Первые виды появились примерно 243-233 млн лет назад. Существа вели различный образ жизни в зависимости от особенностей строения тела и окружающей среды. Среди них были как хищники, так и травоядные. Некоторые виды вели наземный образ жизни, другие обитали под водой, а третьи и вовсе могли летать.",
        "img1": "https://clck.ru/34RZP6",
        "img2": "https://clck.ru/sN8XA"
    })

@app.route('/test')
def test():
    return render_template('new.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login/')
def login():
    form_data = dict(request.args)
    print(form_data)
    if len(form_data) > 0:
        print(form_data['login'])
        print(form_data['password'])
    msg = f'Добро пожаловать, {form_data["login"]}'
    return render_template('home.html', data={'msg': msg})

@app.route('/calc')
def calc():
    status = False
    result = ''
    exchange = ''
    form_data = dict(request.args)
    if len(form_data) > 0:
        status = True
        exchange = form_data['exchange']
        result = float(form_data['rub']) * course[exchange]
    return render_template('calc.html', data={'status': status, 'result': f'{result} {exchange}'})


app.run()
