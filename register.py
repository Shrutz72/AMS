import tkinter as tk
from tkinter import messagebox
from models import add_user

def register_user():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not name or not email or not password:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    try:
        add_user(name, email, password)
        messagebox.showinfo("Success", "Registration successful!")
        register_window.destroy()
    except:
        messagebox.showerror("Error", "User with this email already exists")

def open_register():
    global register_window, name_entry, email_entry, password_entry
    register_window = tk.Toplevel()
    register_window.title("Register")

    tk.Label(register_window, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(register_window)
    name_entry.grid(row=0, column=1)

    tk.Label(register_window, text="Email").grid(row=1, column=0)
    email_entry = tk.Entry(register_window)
    email_entry.grid(row=1, column=1)

    tk.Label(register_window, text="Password").grid(row=2, column=0)
    password_entry = tk.Entry(register_window, show="*")
    password_entry.grid(row=2, column=1)

    tk.Button(register_window, text="Register", command=register_user).grid(row=3, column=1)
