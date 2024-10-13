from csv_file.csv_file import CSVFile
from prettytable import PrettyTable

class UserData:
    def display_data(self):
        users = CSVFile().get_data('Users.csv')
        table = PrettyTable()
        # set table column names
        table.field_names = users[0].keys()
        # set data in table to look good in cosole
        for user in users:
            table.add_row(user.values())

        print(table)