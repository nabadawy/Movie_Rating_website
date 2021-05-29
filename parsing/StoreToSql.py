import csv
import pymysql.cursors

DATABASE_NAME='mydb'

# Connect to the database
connection = pymysql.connect(host='localhost',
                user='root',
                password='nopassword',
                cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}')
        
        # TODO: Should nationality be moved to a separate table and a foreign key be used instead of text?
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {DATABASE_NAME}.cast \
            (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
            first_name NVARCHAR(255), \
            second_name NVARCHAR(255), \
            date_of_birth DATE, \
            nationality VARCHAR(255), \
            role VARCHAR(255), \
            biography NVARCHAR(2000))')
        
        with open('Cast.csv', 'r', newline='') as file:
            csv_data = csv.reader(file)
            next(csv_data)
            for row in csv_data:
                row = [field.replace('"', '\\"') for field in row]  # escape double quotes
                values = f'"{row[0]}", STR_TO_DATE("{row[1]}", "%d %M %Y"), "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}"'

                cursor.execute(f'INSERT INTO {DATABASE_NAME}.cast \
                    (biography, date_of_birth, first_name, nationality, role, second_name) \
                    VALUES ({values})')

    connection.commit()

print ("Done")