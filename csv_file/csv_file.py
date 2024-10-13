import csv
import os

class CSVFile:

    def save_data(self, file_path, header, data):
        #check if id exist in header 
        if not os.path.exists(file_path):
            with open(file_path, 'w', newline='') as csv_file:
                csv_write = csv.DictWriter(csv_file, fieldnames=header)
                csv_write.writeheader()

        with open(file_path, 'a', newline='') as csv_file:
            csv_write = csv.DictWriter(csv_file, fieldnames=header)

            # Check if old data exists
            with open(file_path, 'r', newline='') as read_file:
                csv_reader = csv.DictReader(read_file)
                existing_data = list(csv_reader)
                for record in existing_data:
                    if record['email'] == data[0]['email']:
                        print('Email already exists, please try another.')
                        return False
            last_id = 0
            if existing_data:
                last_id = int(existing_data[-1]['id'])
            
            for record in data:
                last_id += 1
                record['id'] = last_id
                csv_write.writerow(record)
            os.system('cls')
            print('Data saved successfully')
            return True
    
    def verify_login(self, file_path, data):
        if os.path.exists(file_path):
            with open(file_path, mode='r', newline='') as read_file:
                csv_reader  = csv.DictReader(read_file)
                for record in csv_reader:
                    if record['email'] == data['email'] and record['password'] == data['password']:
                        print('Login successful!')
                        return True
            print('Email/ Password is Invalid')
            return False
        else:
            print('File does not exist.')
            return False

    def get_data(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, mode='r', newline='') as read_file:
                csv_reader = csv.DictReader(read_file)
                return list(csv_reader)
               
        else:
            print('File does not exist.')
            return None