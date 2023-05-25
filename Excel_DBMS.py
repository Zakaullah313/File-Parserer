'''
This Python project is developed for converting your CSV files into SQL tables

'''

import mysql.connector
import pandas as pd
import csv

# Build Database connection
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Data123',
    database = 'mydatabase'
)

mycursor = mydb.cursor()

# Create empty table
mycursor.execute('CREATE TABLE IF NOT EXISTS student (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), GR INT)')
mycursor.execute('SHOW DATABASES')

# Read CSV file
with open("Student.csv",'r') as stu:
    data = csv.reader(stu)
    next(data)

# Insert data into table from CSV file
    for i in data:
        id = i[0]
        name = i[1]
        gr = i[2]

        sql = 'INSERT INTO student VALUES (%s, %s, %s)'
        val = (id, name, gr)
        mycursor.execute(sql, val)
        
# Commit the changes in your database
mydb.commit()

# Close the database
mydb.close()