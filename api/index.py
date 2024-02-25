from flask import Flask

app = Flask(__name__)

@app.route('/sign-in')
def signIn():
    return 'sign in!'

@app.route('/sign-up')
def signUp():
    return 'sign up!'

@app.route('/forgot-password')
def forgotPassword():
    return 'forgot password!'