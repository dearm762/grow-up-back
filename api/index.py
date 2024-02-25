from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/sign-in')
def signIn():
    return jsonify({
        "message": "sign in",
        "status": True
    })

@app.route('/sign-up')
def signUp():
    return jsonify({
        "message": "sign up",
        "status": True
    })

@app.route('/forgot-password')
def forgotPassword():
    return jsonify({
        "message": "forgot password",
        "status": True
    })