# Program Name: Assignment5.py
# Course: IT3883/Section 01
#Mina Bayramoglu
# Assignment Number: 5
# Due Date: 4/22/2026
# Purpose: Create a database and insert values from input txt into db. Then calculate avg
#https://www.sqlitetutorial.net/sqlite-python/creating-database/
#https://www.geeksforgeeks.org/python/python-sqlite-create-table/
#https://www.geeksforgeeks.org/dbms/querying-data-from-a-database-using-fetchone-and-fetchall/
import sqlite3

conn = sqlite3.connect("temperature.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS TemperatureData (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Day_Of_Week TEXT,
    Temperature_Value FLOAT
)
""")
#read and insert input txt
with open("Assignment5input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            day = parts[0].strip()
            temp = float(parts[1].strip())

            cursor.execute("""
            INSERT INTO TemperatureData (Day_Of_Week, Temperature_Value)
            VALUES (?, ?)
            """, (day, temp))
conn.commit()

#sunday
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM TemperatureData
WHERE Day_Of_Week = 'Sunday'
""")
sunday_avg = cursor.fetchone()[0]

#thursday
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM TemperatureData
WHERE Day_Of_Week = 'Thursday'
""")
thursday_avg = cursor.fetchone()[0]


print(f"Average Temperature on Thursday: {thursday_avg:.2f}")
print(f"Average Temperature on Sunday: {sunday_avg:.2f}")
conn.close()