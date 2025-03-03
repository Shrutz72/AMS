import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Attendance Window
def attendance_window():
    window = tk.Toplevel()
    window.title("Attendance Management")
    window.geometry("400x300")

    # Label for Date Selection
    date_label = tk.Label(window, text="Select Date (YYYY-MM-DD):")
    date_label.pack(pady=10)
    
    # Date Entry Field
    date_entry = tk.Entry(window)
    date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Default to today's date
    date_entry.pack(pady=5)

    # Function to Mark Attendance
    def mark_attendance():
        date = date_entry.get()
        user_id = 1  # Assuming user_id is 1 for testing; you might get this from logged-in user

        # Insert attendance record
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Insert or Update attendance for the date
        cursor.execute('''
            INSERT INTO attendance (user_id, date, status)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id, date) DO UPDATE SET status=excluded.status
        ''', (user_id, date, "Present"))
        
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Attendance marked for {date} as Present.")

    # Mark Attendance Button
    mark_button = tk.Button(window, text="Mark Attendance", command=mark_attendance)
    mark_button.pack(pady=10)

    # Function to View Attendance
    def view_attendance():
        date = date_entry.get()
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Fetch attendance for the date
        cursor.execute('''
            SELECT status FROM attendance
            WHERE user_id = ? AND date = ?
        ''', (1, date))  # Assuming user_id = 1

        result = cursor.fetchone()
        conn.close()
        
        if result:
            status = result[0]
            messagebox.showinfo("Attendance Record", f"Attendance on {date}: {status}")
        else:
            messagebox.showinfo("Attendance Record", f"No attendance record for {date}.")

    # View Attendance Button
    view_button = tk.Button(window, text="View Attendance", command=view_attendance)
    view_button.pack(pady=10)

# To test independently
if _name_ == "_main_":
    root = tk.Tk()
    attendance_window()
    root.mainloop()