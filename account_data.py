__author__ = 'hanguup'
import sqlite3

def account_table():
    connect = sqlite3.connect('login.db')
    connect.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, PASSWORD NOT NULL)")
    connect.execute("INSERT INTO USERS VALUES(?, ?)", ('superuser', '123'))
    connect.commit()
    result = connect.execute("SELECT * FROM USERS")
    for data in result:
        print('Username: ', data[0])
        print('Password: ', data[1])
    connect.close()

account_table()