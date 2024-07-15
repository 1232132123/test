from flask import Flask, request, jsonify
import json
import jwt

app = Flask(__name__)

SECRET_KEY = 'your_secret_key'

JSON_FILE = 'data_task2.json'

LOGIN_LOG_FILE = 'login_log_task2.txt'

with open(JSON_FILE, 'r') as file:
    logins = json.load(file)

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('login')
    password = request.json.get('password')

    if username in logins and logins[username] == password:
        token = jwt.encode({'user': username}, SECRET_KEY)

        with open(LOGIN_LOG_FILE, 'a') as file:
            file.write(f"{username} {token}\n")

        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run(debug=True)