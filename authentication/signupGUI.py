import tkinter as tk
from tkinter import messagebox
from validation.validation import Validation
from csv_file.csv_file import CSVFile

class SignupGUI:
    def __init__(self, master, geometry):
        self.master = master
        self.master.title('Singup')
        self.master.geometry(geometry)
        self.master.bind(self.onSubmit)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text='Signup', font=('Arial', 16)).pack(pady=10)
        
        tk.Label(self.master, text='Name').pack(pady=5)
        self.name = tk.Entry(self.master, width=50)
        self.name.pack(pady=5)

        tk.Label(self.master, text='Email').pack(pady=5)
        self.email = tk.Entry(self.master, width=50)
        self.email.pack(pady=5)

        tk.Label(self.master, text='Password').pack(pady=5)
        self.password = tk.Entry(self.master, width=50)
        self.password.pack(pady=5)

        tk.Label(self.master, text='Confirm Password').pack(pady=5)
        self.confirm_password = tk.Entry(self.master, width=50)
        self.confirm_password.pack(pady=5)

        tk.Button(self.master, text='Submit', width=50, command=lambda: self.onSubmit()).pack(pady=20)

    def onSubmit(self, event=None):

        if not self.name.get().strip() or not self.email.get().strip() or not self.password.get().strip() or not self.confirm_password.get().strip():
            messagebox.showinfo('Details required', 'Please fill in all the details')
            return 

        if Validation.email(self, self.email.get()):
            messagebox.showinfo('Email', 'Please enter a valid email')
            return

        if self.password.get() == self.confirm_password.get():
            messagebox.showinfo('Password', 'Password and Confirm Password do not match')
            return

        header = ['id', 'name', 'email', 'password']
        data = [{'name': self.name.get(), 'email': self.email.get(), 'password': self.password.get()}]

        if not CSVFile.save_data(self, 'Users.csv', header, data):
            messagebox.showerror('Error', 'Email already exist, please try with different email')
        else:
            messagebox.showinfo('Success', 'Signup successful!')
            self.master.destroy()


