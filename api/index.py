from flask import Flask

app = Flask(__name__)

@app.route('/sign-in')
def home():
    return 'Hello, World!'

@app.route('/sign-uo')
def home():
    return 'Hello, World!'

@app.route('/forgot-password')
def home():
    return 'Hello, World!'