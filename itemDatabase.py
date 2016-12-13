__author__ = 'hanguup'

import sqlite3

def account_table():
    connect = sqlite3.connect('itemslist.db')
    connect.execute("CREATE TABLE ITEMS(SELLER TEXT NOT NULL, ITEMNAME TEXT NOT NULL, PRICE FLOAT NOT NULL, DESCRIPTION)")
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user0','fruit', '123', 'orange'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user1','fruit', '123', 'orange'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user2','car', '10000', 'Honda'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user3','fruit', '123', 'apples'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user4','car', '10000', 'Honda'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user5','fruit', '123', 'apples'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user6','car', '10000', 'BMW'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user7','fruit', '123', 'banana'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user8','car', '10000', 'TANK'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user9','fruit', '123', 'blackberry'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('user10','car', '10000', 'AIRPLANE'))
    connect.commit()
    result = connect.execute("SELECT * FROM ITEMS")
    for data in result:
        print('name: ', data[0])
        print('item: ', data[1])
        print('price: ', data[2])
        print('description: ', data[3])
    connect.close()

def addmessage_database():
    for i in range(11):
        user_message = 'user'+ str(i) + '.db'
        connect2 = sqlite3.connect(user_message)
        connect2.execute("CREATE TABLE MESSAGES(MESSAGE TEXT)")
addmessage_database()
account_table()