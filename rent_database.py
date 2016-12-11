__author__ = 'hanguup'
import sqlite3

def account_table():
    connect = sqlite3.connect('itemslist.db')
    connect.execute("CREATE TABLE RENTITEMS(SELLER TEXT NOT NULL, ITEMNAME TEXT NOT NULL, PRICE FLOAT NOT NULL, DESCRIPTION)")
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('superuser','house', '12300', 'Manhattan'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('superuser','car', '10000', 'Honda'))
    connect.commit()
    result = connect.execute("SELECT * FROM ITEMS")
    for data in result:
        print('name: ', data[0])
        print('item : ', data[1])
        print('price: ', data[2])
        print('description: ', data[3])
    connect.close()

account_table()