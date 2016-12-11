__author__ = 'hanguup'
import sqlite3

def account_table():
    connect = sqlite3.connect('login.db')
    #connect.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,PASSWORD NOT NULL, MONEY REAL, RATING REAL, ACTIVATE INTEGER, FLAG INTEGER)")
    #connect.execute("INSERT INTO USERS VALUES(?, ?,?,?,?,?)", ('sample1', '123',0,5,1,0))
    #connect.commit()
    result=connect.execute("SELECT * FROM USERS")
    for data in result:
        print(data[0])
        print(data[1])
        print(data[2])
        print(data[3])
        print(data[4])
        print(data[5])
    connect.close()
account_table()