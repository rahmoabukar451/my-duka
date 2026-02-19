from flask import Flask

#flask instance
app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"


@app.route('/login')
def login():
    return "login page"

@app.route('/products')
def products():
    return "prodcts page"

app.run()

