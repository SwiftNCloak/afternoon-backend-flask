# VULNERABLE. Fix this code.

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Vulnerable: No password hashing
def init_db():
    conn = sqlite3.connect('users.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Vulnerable: No input validation
        conn = sqlite3.connect('users.db')
        conn.execute(f"INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

        conn.commit()
        conn.close()
        return "User Registered"
    return render_template('form.html')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
