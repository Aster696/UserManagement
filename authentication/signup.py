import getpass
from csv_file.csv_file import CSVFile
from validation.validation import Validation
from .login import Login
import os

class Signup:

    def form(self):
        os.system('cls')
        print('** Singup ** \n')
        name = input('Enter your name: ')
        email = input('Enter your email: ')
        # check if email is valid
        if not Validation.email(self, email):
            print('Please enter valid email')
            return self.try_again()
        password = getpass.getpass('Password: ')
        confirm = getpass.getpass('Confirm Password: ')

        # check if pass and con_pass match
        if password != confirm:
            print('Passwords do not match')
            return self.try_again() 
        
        header = ['id', 'name', 'email', 'password']
        data = [{'name': name, 'email': email, 'password': password}]
        if not CSVFile.save_data(self, 'Users.csv', header, data):
            return self.try_again() 
        else:
            return Login().form()

    def try_again(self):
        yes = input('Would you like to try again? Press y/n: ') 
        if yes.lower() in ['y', 'yes']:
            self.form()
