import sqlite3
conn = sqlite3.connect('appdata.db')
cursor = conn.execute("Select ID, NAME, AGE, ADDRESS, PHONE, GENDER, CNNRESULT  from AppointmentReqs")

print("All the details of the database")
for row in cursor:
    print(f"ID = {row[0]}")
    print(f"NAME = {row[1]}")
    print(f"AGE = {row[2]}")
    print(f"ADDRESS = {row[3]}")
    print(f"PHONE = {row[4]}")
    print(f"GENDER = {row[5]}")
    print(f"CNN RESULT = {row[6]}")
    print() # For empty line!

conn.close()