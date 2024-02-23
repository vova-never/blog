<<<<<<< HEAD
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


=======
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


>>>>>>> 1a573c7e8f152bc7db815f4bbfe9475f3b816ce2
    