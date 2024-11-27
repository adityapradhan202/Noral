# Script to create database and tables in it!

import sqlite3

try:
    conn = sqlite3.connect('appdata.db')
    print("-> Database has been created!")

    # Table for appointment requests
    conn.execute("Create table AppointmentReqs(ID INT, NAME TEXT, AGE INT, ADDRESS TEXT, PHONE TEXT, GENDER TEXT, CNNRESULT TEXT);")
    print("-> AppointmentReqs database has been created!")

    conn.close()
    print("-> Connection closed!")
except Exception as e:
    print(f"Some exception occured: {e}")

