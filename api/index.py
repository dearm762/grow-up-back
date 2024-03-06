from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
import pymysql
from ssid import generateRandomSsid

app = Flask(__name__)
CORS(app)

connection = pymysql.connect(
    host='185.22.67.20',
    user='db-admin',
    password='Aktau7292',
    db='grow-up',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/sign-up', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    surname = data.get('surname')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')
    ssid = generateRandomSsid()

    try:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, surname, email, phone, passwordhashed, ssid) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, surname, email, phone, hashed_password, ssid))
            connection.commit()

        return jsonify({'message': 'User registered successfully', 'ssid': ssid}), 201

    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/sign-in', methods=['POST'])
def signin():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE email = %s"
            cursor.execute(sql, email)
            user = cursor.fetchone()

            if user:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if user['passwordhashed'] == hashed_password:
                    ssid = generateRandomSsid()
                    update_sql = "UPDATE users SET ssid = %s WHERE email = %s"
                    cursor.execute(update_sql, (ssid, email))
                    connection.commit()
                    return jsonify({'message': 'Login successful', 'ssid': ssid}), 200
                else:
                    return jsonify({'message': 'Incorrect password'}), 401
            else:
                return jsonify({'message': 'User not found'}), 404

    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)