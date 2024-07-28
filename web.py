from flask import Flask, request, render_template, redirect, url_for, jsonify
import sqlite3
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)

# Initialize the database and create the table if it doesn't exist
def init_db():
    conn = sqlite3.connect('serial_keys.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS keys
                 (serial_key TEXT, email TEXT, expiry_date TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Check if the email address already exists in the database
def email_exists(email):
    conn = sqlite3.connect('serial_keys.db')
    c = conn.cursor()
    c.execute("SELECT 1 FROM keys WHERE email = ?", (email,))
    exists = c.fetchone() is not None
    conn.close()
    return exists

# Generate a serial key and save it to the database
def generate_serial_key(email, days):
    serial_key = str(uuid.uuid4()).replace('-', '').upper()[:12]  # Generate a 12-character key
    expiry_date = (datetime.now() + timedelta(days=days)).strftime('%Y-%m-%d')
    conn = sqlite3.connect('serial_keys.db')
    c = conn.cursor()
    c.execute("INSERT INTO keys (serial_key, email, expiry_date) VALUES (?, ?, ?)", (serial_key, email, expiry_date))
    conn.commit()
    conn.close()
    return serial_key

# Home page and form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        days = int(request.form['days'])

        if email_exists(email):
            return render_template('index.html', error="This email address is already registered.")
        
        serial_key = generate_serial_key(email, days)
        return render_template('key_generated.html', serial_key=serial_key, days=days)
    
    return render_template('index.html')

# Check if the serial key is valid
@app.route('/check_serial_key', methods=['GET'])
def check_serial_key():
    key = request.args.get('key')
    if not key:
        return jsonify({'error': 'No key provided'}), 400

    conn = sqlite3.connect('serial_keys.db')
    c = conn.cursor()
    c.execute("SELECT expiry_date FROM keys WHERE serial_key=?", (key,))
    result = c.fetchone()
    conn.close()

    if result:
        expiry_date = datetime.strptime(result[0], '%Y-%m-%d')
        if expiry_date > datetime.now():
            return jsonify({'valid': True})
    return jsonify({'valid': False})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
