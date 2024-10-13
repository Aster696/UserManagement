from csv_file.csv_file import CSVFile
import os

class Login:

    def form(self):
        os.system('cls')
        print('** Login **\n')
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        if CSVFile.verify_login(self, 'Users.csv', {'email': email, 'password': password}):
            return True
        else:
            self.try_again()
            return False
            
    def try_again(self):
        yes = input('Would you like to try again? Press y/n: ') 
        if yes.lower() in ['y', 'yes']:
            self.form()