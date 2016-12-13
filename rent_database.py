__author__ = 'hanguup'
import sqlite3

def account_table():
    connect = sqlite3.connect('rentlist.db')
    connect.execute("CREATE TABLE RENTITEMS(SELLER TEXT NOT NULL, ITEMNAME TEXT NOT NULL, PRICE FLOAT NOT NULL, DESCRIPTION)")
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user0','car', '10000', 'Honda'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user1','fruit', '123', 'orange'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user2','car', '10000', 'Honda'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user3','fruit', '123', 'apples'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user4','car', '10000', 'Honda'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user5','fruit', '123', 'apples'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user6','car', '10000', 'BMW'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user7','fruit', '123', 'banana'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user8','car', '10000', 'TANK'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user9','fruit', '123', 'blackberry'))
    connect.execute("INSERT INTO RENTITEMS VALUES(?, ?, ?, ?)", ('user10','car', '10000', 'AIRPLANE'))
    connect.commit()
    result = connect.execute("SELECT * FROM RENTITEMS")
    for data in result:
        print('name: ', data[0])
        print('item : ', data[1])
        print('price: ', data[2])
        print('description: ', data[3])
    connect.close()

account_table()