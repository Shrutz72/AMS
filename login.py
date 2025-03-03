import tkinter as tk
from tkinter import messagebox
from models import authenticate_user
from ui.dashboard import open_dashboard

def login():
    email = email_entry.get()
    password = password_entry.get()
    user = authenticate_user(email, password)

    if user:
        messagebox.showinfo("Login Success", f"Welcome, {user[1]}!")
        open_dashboard(user)
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials")

root = tk.Tk()
root.title("Login")

tk.Label(root, text="Email").grid(row=0, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

tk.Button(root, text="Login", command=login).grid(row=2, column=1)
