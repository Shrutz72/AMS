import sqlite3

# Connect to SQLite database
def connect_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                     )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                        id INTEGER PRIMARY KEY,
                        user_id INTEGER NOT NULL,
                        date TEXT NOT NULL,
                        status TEXT NOT NULL,
                        FOREIGN KEY (user_id) REFERENCES users(id)
                     )''')
    conn.commit()
    conn.close()

# Add a new user
def add_user(name, email, password):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()

# Authenticate user
def authenticate_user(email, password):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        return cursor.fetchone()

# Mark attendance
def mark_attendance(user_id, status):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO attendance (user_id, date, status) VALUES (?, date('now'), ?)", (user_id, status))
        conn.commit()

# Get attendance for a specific date
def get_attendance_by_date(user_id, date):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM attendance WHERE user_id=? AND date=?", (user_id, date))
        return cursor.fetchone()
