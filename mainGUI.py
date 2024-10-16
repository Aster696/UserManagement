import tkinter as tk
from tkinter import messagebox
from authentication.signup import Signup
from authentication.signupGUI import SignupGUI

class UserManagement:
    def __init__(self, master):
        self.master = master
        self.is_loggedin = False
        self.master.title('User Management')
        # calculate the screen size and set the widget to be 50% of screen
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        window_width = int(screen_width * 0.5)
        window_height = int(screen_height * 0.5)

        self.geometry = f"{window_width}x{window_height}+{(screen_width-window_width) // 2}+{(screen_height - window_height) // 2}"
        master.geometry(self.geometry)

        self.create_widgets(window_width)

    def create_widgets(self, window_width):
        tk.Label(self.master, text='User Management', font=('Arial', 16)).pack(pady=10)
        # show options and set button width
        tk.Button(self.master, text='Signup', width=50, command=lambda: self.show_signup()).pack(pady=5, padx=10)
        tk.Button(self.master, text='Login', width=50, command='').pack(pady=5, padx=10)
        tk.Button(self.master, text='Display Users', width=50, command='').pack(pady=5, padx=10)
        tk.Button(self.master, text='Exit', width=50, command=self.master.quit).pack(pady=5, padx=10)
    
    def show_signup(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        SignupGUI(self.master, self.geometry)


if __name__ == "__main__":
    root = tk.Tk()
    user_mgmt_app = UserManagement(root)
    root.mainloop()