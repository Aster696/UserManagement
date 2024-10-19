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
        for i, user in enumerate(users):
            row_tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            self.tree.insert('', tk.END, values=(user['id'], user['name'], user['email'], user['password']), tags=(row_tag,))

        # Pack the Treeview widget with padding and expand options
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)