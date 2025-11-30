import sqlite3
import csv
#install pandas

#Create the data basa
connection = sqlite3.connect('Cloud_Data.db')
cursor = connection.cursor()


# Creates the table is one isn't there
sql_create_table = """
CREATE TABLE IF NOT EXISTS Cloud_Data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Temperature_Fahrenheit REAL,
    Humidity REAL,
    Date_Time TEXT
);
"""

cursor.execute(sql_create_table)
connection.commit()


#open the file and reads from it
with open("Stored_Data.csv", "r") as file:
    reader = csv.reader(file)
    #reads it line by line
    for row in reader:
        temperature = float(row[0])
        humidity = float(row[1])
        date_time = row[2]

        cursor.execute(
            "INSERT INTO Cloud_Data (Temperature_Fahrenheit, Humidity, Date_Time) VALUES (?, ?, ?)",
            (temperature, humidity, date_time)
        )

connection.commit()
connection.close()

