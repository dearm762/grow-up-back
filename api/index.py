from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/sign-in', methods=['POST'])
def signIn():
    request_data = request.get_json()
    return jsonify({
        "message": "sign in",
        "status": True,
        "data": request_data
    })

@app.route('/sign-up', methods=['POST'])
def signUp():
    return jsonify({
        "message": "sign up",
        "status": True
    })

@app.route('/forgot-password', methods=['POST'])
def forgotPassword():
    return jsonify({
        "message": "forgot password",
        "status": True
    })