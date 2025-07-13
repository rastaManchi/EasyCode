from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/add_cookie')
def add_cookie():
    response = make_response(render_template('index.html'))
    response.set_cookie('sessionID', 'kfghkdfghbkdh;vmcvvbxckvsdpfsdnikfvbsdk:sdffsdjh', max_age=40)
    return response

@app.route('/get_cookie')
def get_cookie():
    print(request.cookies.get('sessionID'))
    return render_template('index.html')

app.run(debug=True)