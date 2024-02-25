from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from psycopg2 import connect
import random
import string
import hashlib

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

def generate_ssid(length=50):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/sign-in', methods=['POST'])
def signIn():
    request_data = request.get_json()
    email = request_data.get('email')
    password = request_data.get('password')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, hash_password(password)))
    user = cursor.fetchone()
    cursor.close()
    if user:
        ssid = user[5]
        return jsonify({
            "message": "Sign in successful",
            "status": True,
            "ssid": ssid
        })
    else:
        return jsonify({
            "message": "Invalid email or password",
            "status": False
        })

@app.route('/sign-up', methods=['POST'])
def signUp():
    request_data = request.get_json()
    name = request_data.get('name')
    surname = request_data.get('surname')
    email = request_data.get('email')
    password = request_data.get('password')

    hashed_password = hash_password(password)
    
    ssid = generate_ssid()

    try:
        cursor = db.cursor()
        cursor.execute("INSERT INTO users (name, surname, email, password, ssid) VALUES (%s, %s, %s, %s, %s)", (name, surname, email, hashed_password, ssid))
        db.commit()
        cursor.close()
        return jsonify({
            "message": "Sign up successful",
            "status": True,
            "ssid": ssid
        })
    except psycopg2.IntegrityError as e:
        # Duplicate email error
        db.rollback()
        return jsonify({
            "message": "Email already exists",
            "status": False
        })

@app.route('/forgot-password', methods=['POST'])
def forgotPassword():
    return jsonify({
        "message": "forgot password api still is not ready",
        "status": True
    })

@app.route('/is-token-exists', methods=['POST'])
def isTokenExists():
    return jsonify({
        "message": "is there any user with this token",
        "status": True
    })


if __name__ == "__main__":
    app.run()