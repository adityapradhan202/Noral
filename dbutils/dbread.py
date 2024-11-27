import pandas as pd
import sqlite3


def display_db():
    conn = sqlite3.connect('appdata.db')
    df = pd.read_sql_query(sql="Select ID, NAME, AGE, ADDRESS, PHONE, GENDER, CNNRESULT from AppointmentReqs", con=conn)
    conn.close()

    return df

if __name__ == "__main__":
    print(display_db())