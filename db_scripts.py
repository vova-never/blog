
import sqlite3

db_name = "db.db"
connection = None
cursor = None

def open():
    global connection,cursor
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

def close():
    cursor.close()
    connection.close()

import sqlite3

db_name = "db.db"
connection = None
cursor = None

def open():
    global connection,cursor
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

def close():
    cursor.close()
    connection.close()

def getUser():
    open()
    cursor.execute(''' SELECT * FROM user''')
    user = cursor.fetchone()
    close()
    return user
