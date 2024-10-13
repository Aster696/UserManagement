from authentication.signup import Signup
from authentication.login import Login
from user_data.user_data import UserData
import os
import sys

class UserManagement:

    is_loggedin = False
    def __init__(self) -> None:
        self.main()

    def menu(self):
        os.system('cls')
        print('** User Management **')
        print('1. Signup')
        print('2. Login')
        print('3. Display Users')
        option = input('Enter your option: ')
        match option:
            case '1':
                Signup().form()
            case '2':
                self.is_loggedin = Login().form() 
            case '3':
                if self.is_loggedin: 
                    UserData().display_data()
                else: 
                    self.is_loggedin = Login().form() 
            case _:
                print("Invalid option")
        yes = input('Wourld you like to continue with other options? Press y/n: ')
        if yes.lower() in ['y', 'yes']:
            self.menu()
        else:
            print('Exiting the program. Thank you!')
            sys.exit()
    
    def menu_GUI(self):
        pass

    def main(self):
        self.menu()


# Initialize the main class
user = UserManagement()
user.main()