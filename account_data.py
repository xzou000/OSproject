___author__ = 'hanguup'
import sqlite3

def account_table():
    connect = sqlite3.connect('login.db')
    connect.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,PASSWORD NOT NULL, MONEY REAL, ACTIVATE INTEGER,\
     FLAG INTEGER, RATE FLOAT, NUMRATE INT, COMPLAINT INT, SUSPENDED INT, VIP INT)")
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('sample1', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user0', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user1', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user2', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user3', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user4', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user5', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user6', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user7', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user8', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user9', '123',0,1,0,0,0,0,0,0))
    connect.execute("INSERT INTO USERS VALUES(?,?,?,?,?,?,?,?,?,?)", ('user10', '123',0,1,0,0,0,0,0,0))
    connect.commit()

    connect.close()
account_table()