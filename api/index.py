from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from psycopg2 import connect

app = Flask(__name__)

db = connect(
    dbname="rqskigmw",
    user="rqskigmw",
    password="Ph3vQzCXoigc-g-dYHrVwYTD7lMPkeJn",
    host="surus.db.elephantsql.com",
    port="5432"
)

cursor = db.cursor()

cursor.execute("SELECT version();")

record = cursor.fetchone()
print("You are connected to - ", record)

cursor.close()
db.close()

@app.route('/')
def main():
    return render_template('index.html')

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