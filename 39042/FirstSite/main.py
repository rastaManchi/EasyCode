from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/frogs')
def frogs():
   return render_template('home.html', data={
        'name': 'Лягушки',
        'title': 'Лягушки',
        'text': 'Лягушки — общеупотребительное название группы животных из отряда бесхвостых земноводных. В широком смысле термин «лягушка» относится ко всем представителям отряда бесхвостых. В узком смысле это название применяется по отношению к представителям семейства настоящих лягушек. Личинки лягушек называются головастиками.',
        'img1': 'https://clck.ru/34RZLn',
        })


@app.route('/cats')
def cats():
   return render_template('home.html', data={
        'name': 'Кошки',
        'title': 'Кошки',
        'text': 'Кошки все прекрасные и пушистые',
        'img1': 'https://static.tildacdn.com/tild3163-3066-4534-b633-323361313535/image.png',
        })

app.run()
