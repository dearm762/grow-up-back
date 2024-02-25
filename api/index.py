from flask import Flask, jsonify, request, render_template
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

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/sign-in', methods=['POST'])
def signIn():
    request_data = request.get_json()
    email = request_data.get('email')
    password = request_data.get('password')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return jsonify({
            "message": "Sign in successful",
            "status": True,
            "user": {
                "email": user[1],  # Assuming email is at index 1 in the result
                # Add more fields here if needed
            }
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
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, surname, email, password) VALUES (%s, %s, %s, %s)", (name, surname, email, password))
    db.commit()
    cursor.close()
    return jsonify({
        "message": "Sign up successful",
        "status": True
    })

@app.route('/forgot-password', methods=['POST'])
def forgotPassword():
    # You can implement forgot password functionality here
    return jsonify({
        "message": "forgot password",
        "status": True
    })

if __name__ == "__main__":
    app.run()
