from flask import Flask, make_response, request


app = Flask(__name__)

@app.route('/') # http://127.0.0.1:5000/
def home():
    cookies = request.cookies
    my = cookies.get("session")
    if my:
        return my
    else:
        return "<a href='/login'>auth</a>"

@app.route('/login') # http://127.0.0.1:5000/news
def news():
    response = make_response('201')
    response.set_cookie("session", "cookie_value", max_age=60)
    return response

app.run()
