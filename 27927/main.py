from flask import Flask, render_template

app = Flask(__name__)

@app.route('/frogs/')
def frogs():
    return '''<h1>Лягушки</h1>
<p><a href="/">На главную</a></p>
<p>Лягушки — общеупотребительное название группы животных из отряда бесхвостых земноводных. В широком смысле термин «лягушка» относится ко всем представителям отряда бесхвостых. В узком смысле это название применяется по отношению к представителям семейства настоящих лягушек. Личинки лягушек называются головастиками.</p>
<h2>Фотографии</h2>
<p><img src="https://clck.ru/34RZLn" width="400"><p>
<p><img src="https://clck.ru/34RZM8" width="400"><p>
'''


@app.route('/snails/')
def snails():
    return '''<h1>Улитки</h1>
<p><a href="/">На главную</a></p>
<p>Ули́тки — общеупотребительное название брюхоногих моллюсков (лат. Gastropoda), обладающих наружной раковиной.</p>
<h2>Фотографии</h2>
<p><img src="https://clck.ru/34RZMp" width="400"><p>
<p><img src="https://clck.ru/34RZNG" width="400"><p>
'''


@app.route('/dynos/')
def dynos():
    return '''<h1>Динозавры</h1>
<p><a href="/">На главную</a></p>
<p>Динозавры – это рептилии, принадлежащие к подклассу архозавров. Первые виды появились примерно 243-233 млн лет назад. Существа вели различный образ жизни в зависимости от особенностей строения тела и окружающей среды. Среди них были как хищники, так и травоядные. Некоторые виды вели наземный образ жизни, другие обитали под водой, а третьи и вовсе могли летать.</p>
<h2>Фотографии</h2>
<p><img src="https://clck.ru/34RZP6" width="400"><p>
<p><img src="https://clck.ru/sN8XA" width="400"><p>
'''

app.run()

