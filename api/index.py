from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def main():
    return """
        <h1>KeepInTouch server greeting page!</h1>
        <p>You can send requests to:</p>
        <a href='/sign-in'>/sign-in</a>
        <br>
        <a href='/sign-up'>/sign-up</a>
        <br>
        <a href='/forgot-password'>/forgot-password</a>
     """

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


if __name__ == "__main__":
    app.run()