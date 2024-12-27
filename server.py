from flask import Flask

app = Flask(__name__)


@app.route("/name/",defaults={'username':'Guest'})
@app.route("/name/<username>")
def hello(username):
    return "Hello, World!"+username