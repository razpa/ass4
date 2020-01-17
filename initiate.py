import _sqlite3
import os
import atexit
import sys

db_exist = os.path.isfile('moncafe.db')  # define databise
if db_exist:
    os.remove('moncafe.db')  # delete database if exist

dbcon = _sqlite3.connect('moncafe.db')
cursor = dbcon.cursor()


# def close_db():
#     dbcon.connect()
#     dbcon.close()
#     os.remove('moncafe.db')


# atexit.register(close_db)


def inserttodb(line):
    splited = line.split(", ")
    what = splited[0]
    if what == 'C':  # coffee stand
        cursor.execute("INSERT INTO Coffee_stands values(?,?,?)", splited[1:])  # insert to Coffee stand

    if what == 'S':  # Suppliers
        cursor.execute("INSERT INTO Suppliers values(?,?,?)", splited[1:])  # insert to Coffee stand

    if what == 'E':  # Employees
        cursor.execute("INSERT INTO Employees values(?,?,?,?)", splited[1:])  # insert to Coffee stand

    if what == 'P':  # Products
        cursor.execute("INSERT INTO Products values(?,?,?,?)", splited[1:])  # insert to Coffee stand


def createtables():
    cursor.execute("""CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY,
                                                location TEXT NOT NULL,
                                                number_of_employees INTEGER)""")

    cursor.execute("""CREATE TABLE Suppliers(id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL,
                                            contact_information TEXT)""")

    cursor.execute("""CREATE TABLE Employees(id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL,
                                            salary REAL NOT NULL,
                                            coffee_stand INTEGER REFERENCES Coffee_stand(id))""")

    cursor.execute("""CREATE TABLE Products(id INTEGER PRIMARY KEY,
                                               desctiption TEXT NOT NULL,
                                               price REAL NOT NULL,
                                               quantity INTEGER NOT NULL)""")

    cursor.execute("""CREATE TABLE Activities(product_id INTEGER REFERENCES Products(id),
                                               quantity INTEGER NOT NULL,
                                               activator_id INTEGER NOT NULL,
                                               date DATE NOT NULL)""")


def main(args):
    createtables()
    config = args[0]
    with open(config) as inputfile:
        for line in inputfile:
            inserttodb(line)


if __name__ == '__main__':
    main(sys.argv)