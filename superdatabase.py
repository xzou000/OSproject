__author__ = 'hanguup'
import sqlite3

def account_table():
    connect = sqlite3.connect('superuser.db')
    connect.execute("CREATE TABLE USERMESSAGES(USERNAME TEXT NOT NULL,MESSAGE TEXT)")
    connect.commit()

    connect.close()
account_table()