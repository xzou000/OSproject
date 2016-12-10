__author__ = 'hanguup'

import sqlite3

def account_table():
    connect = sqlite3.connect('itemslist.db')
    connect.execute("CREATE TABLE ITEMS(ITEMNAME TEXT NOT NULL, PRICE FLOAT NOT NULL, DESCRIPTION)")
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?)", ('fruit', '123', 'apples'))
    connect.commit()
    result = connect.execute("SELECT * FROM ITEMS")
    for data in result:
        print('item: ', data[0])
        print('price: ', data[1])
        print('description: ', data[2])
    connect.close()

account_table()