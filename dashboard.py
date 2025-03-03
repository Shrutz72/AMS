import tkinter as tk
from models import mark_attendance
from ui.attendance import open_view_attendance_by_date
from ui.register import open_register

def open_dashboard(user):
    dashboard = tk.Tk()
    dashboard.title("Dashboard")

    tk.Label(dashboard, text=f"Welcome, {user[1]}").pack()

    # Mark Attendance Button
    def mark():
        mark_attendance(user[0], "Present")
        tk.messagebox.showinfo("Attendance", "Attendance marked as present")

    tk.Button(dashboard, text="Mark Attendance", command=mark).pack()
    tk.Button(dashboard, text="View Attendance by Date", command=lambda: open_view_attendance_by_date(user[0])).pack()
    tk.Button(dashboard, text="Register New User", command=open_register).pack()
