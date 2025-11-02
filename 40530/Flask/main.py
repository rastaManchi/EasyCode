from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET" ,"POST"])
def check():
    if request.method == "POST":
        data = dict(request.form)
        login = data['login']
        password = data['password']
        print(login, password)
        return render_template('index.html', data={
            "text": "Вы успешно авторизовались"
        })
    return render_template('index.html', data={
            "text": "Вход"
        })

app.run()