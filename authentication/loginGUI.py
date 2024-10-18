import tkinter as tk
from tkinter import messagebox
from csv_file.csv_file import CSVFile

class LoginGUI:
    
    def __init__(self, master, geometry):
        self.master = master
        self.master.title('Login')
        self.master.geometry(geometry)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text='Login', font=('Arial', 16)).pack(pady=10)

        tk.Label(self.master, text='Email').pack(pady=5)
        self.email = tk.Entry(self.master, width=50)
        self.email.pack(pady=5)

        tk.Label(self.master, text='Password').pack(pady=5)
        self.password = tk.Entry(self.master, width=50)
        self.password.pack(pady=5)

        tk.Button(self.master, text='Submit', width=50, command=lambda: self.onSubmit()).pack(pady=20)

    def onSubmit(self):
        if CSVFile.verify_login(self, 'Users.csv', {'email': self.email, 'password': self.password}):
            messagebox.showinfo('Login successful!')
            # send to display users widget