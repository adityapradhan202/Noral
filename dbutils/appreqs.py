# Operations for the table named 'AppointmentReqs'

import sqlite3

def get_new_id():
    with open("last_index.txt", "r") as file:
        val = file.read()
        val = int(val)
        return val + 1

def new_request(name, age, 
                address, phone, gender, cnn_result,
                table_name='AppointmentReqs'):
    
    id = get_new_id()
    conn = sqlite3.connect('appdata.db')
    query = f"Insert into {table_name}(ID, NAME, AGE, ADDRESS, PHONE, GENDER, CNNRESULT) VALUES({id}, '{name}', {age}, '{address}', '{phone}', '{gender}', '{cnn_result}')"

    conn.execute(query)
    conn.commit()
    conn.close()

    with open('last_index.txt', 'w') as file:
        id = str(id)
        file.write(id)

if __name__ == "__main__":
    new_request(name="Aditya Pradhan", age=21,
                address='a712',
                phone="9871089296",
                gender="male",
                cnn_result="gingivitis")
    
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







