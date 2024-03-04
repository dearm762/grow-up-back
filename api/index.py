from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random
import string
import hashlib
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)

db = mysql.connector.connect(
    host="185.22.67.20:3306",
    user="db_admin",
    password="Aktau7292",
    database="grow-up-course"
)

cursor = db.cursor()

cursor.execute("SELECT VERSION()")
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
    except mysql.connector.IntegrityError as e:
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