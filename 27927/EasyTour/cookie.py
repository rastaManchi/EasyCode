from flask import Flask, render_template, request, make_response

app = Flask(__name__)


# response = make_response(render_template('cookies.html'))
# response.set_cookie('a', 'b', max_age=40)
# request.cookies.get('a')


@app.route('/')
def home():
    cookie_username = request.cookies.get('name')
    cookie_usersurname = request.cookies.get('surname')
    if cookie_username and cookie_usersurname:
        print('куки есть')
    else:
        print('куки нет')
        response = make_response(render_template('cookies.html'))
        response.set_cookie('name', 'Bulat', max_age=20)
        response.set_cookie('surname', 'Zakirov', max_age=20)
        return response
    return render_template('cookies.html')

app.run(debug=True)