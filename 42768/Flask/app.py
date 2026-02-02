from flask import Flask, render_template, request


app = Flask(__name__)


course = {
    'EUR': 77,
    'USD': 63,
    'UZS': 0.00692,
    'GBP': 98,
}


@app.route('/')
def welcome():
    return render_template('index.html', data={
        'title': 'ЯБлоко', 
        'content': 'Если ты видишь это сообщение, значит сервер работает.',
        'img': 'https://avatars.mds.yandex.net/i?id=8baaa2b8e6bb9ed857ec28a7e1f1c9e6df4d6947-5844149-images-thumbs&n=13'
    })
    
@app.route('/dynos')
def dynos():
    return render_template('index.html', data={
        'title': 'Динозавры',
        'content': 'Диноза́вры[1] (лат. Dinosauria) — группа архозавров из клады авеметатарзалий. Динозавры возникли в триасовом периоде, между 243 млн и 233,23 млн лет назад, и стали доминирующими наземными позвоночными после триасово-юрского вымирания 201 млн лет назад; их доминирование продолжалось на протяжении остальной части мезозойской эры, в течение юрского и мелового периодов. ',
        'img': 'https://news-img.gismeteo.st/ru/2025/06/ChatGPT-Image-24-ijun.-2025-g.-23_03_15.png'
    })
    


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        
        data = request.form
        username = data.get('username')
        password = data.get('password')
        
        return render_template('index.html', data={
            'title': username,
            'content': password,
            'img': 'https://news-img.gismeteo.st/ru/2025/06/ChatGPT-Image-24-ijun.-2025-g.-23_03_15.png'
        })
    return render_template('signin.html')

@app.route('/converter/')
def converter():
    data = request.args
    if len(data) > 0:
        summ = float(data.get('summ'))
        currency = data.get('currency')
        new_summ = summ * course[currency]
        return render_template('converter.html', data={'summ': new_summ})
    return render_template('converter.html', data = {'summ': 0})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    
