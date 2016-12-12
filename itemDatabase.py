__author__ = 'hanguup'

import sqlite3

def account_table():
    connect = sqlite3.connect('itemslist.db')
    connect.execute("CREATE TABLE ITEMS(SELLER TEXT NOT NULL, ITEMNAME TEXT NOT NULL, PRICE FLOAT NOT NULL, DESCRIPTION)")
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser1','fruit', '123', 'orange'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser2','car', '10000', 'Honda'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser3','fruit', '123', 'apples'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser4','car', '10000', 'Honda'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser5','fruit', '123', 'apples'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser6','car', '10000', 'BMW'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser7','fruit', '123', 'banana'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser8','car', '10000', 'TANK'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser9','fruit', '123', 'blackberry'))
    connect.execute("INSERT INTO ITEMS VALUES(?, ?, ?, ?)", ('superuser10','car', '10000', 'AIRPLANE'))
    connect.commit()
    result = connect.execute("SELECT * FROM ITEMS")
    for data in result:
        print('name: ', data[0])
        print('item: ', data[1])
        print('price: ', data[2])
        print('description: ', data[3])
    connect.close()

account_table()