___author__ = 'hanguup'
import sqlite3

def account_table():
    connect = sqlite3.connect('login.db')
    connect.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,PASSWORD NOT NULL, MONEY REAL, ACTIVATE INTEGER, FLAG INTEGER)")
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?)", ('sample1', '123',0,1,0))
    connect.commit()

    connect.close()
account_table()