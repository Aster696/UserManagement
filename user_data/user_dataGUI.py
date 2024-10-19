import tkinter as tk
from tkinter import ttk
from csv_file.csv_file import CSVFile

class UserDataGUI:

    def __init__(self, master, geometry):
        self.master = master
        self.master.title('User list')
        self.master.geometry(geometry)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text='User List', font=('Arial', 16)).pack(pady=10)
        users = CSVFile.get_data(self, 'Users.csv')
        # display heading of table
        columns = ('ID', 'Name', 'Email', 'Password')
        self.tree = ttk.Treeview(self.master, columns=columns, show='headings')

        for col in columns:
            self.tree.heading(col, text=col)

        # dispay data
        for user in users:
            self.tree.insert('', tk.END, values=(user['id'], user['name'], user['email'], user['password']))
        
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)