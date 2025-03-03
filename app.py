import sqlite3
from ui.login import root  # Import the root from the login.py file

# Ensure the database and tables are created
def setup_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()  # Call the function to setup database
    root.mainloop()  # Start the Tkinter event loop
