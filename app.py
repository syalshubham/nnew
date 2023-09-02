from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello1")
def hello_world1():
    return "<h1>Hello, World1!</h1>"

@app.route("/hello2")
def hello_world2():
    return "<h1>Hello, World2!</h1>"

@app.route("/test")
def test_fun():
    a = 11
    return "this is a value equals to {}".format(a)

@app.route("/input_url")
def request_func():
    data = request.args.get("x")
    return "THe input data recieved is {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
