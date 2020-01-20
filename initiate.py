import _sqlite3
import os
import atexit
import sys


db_exist = os.path.isfile('moncafe.db')  # define databise
if db_exist:
    os.remove('moncafe.db')  # delete database if exist
    print("removed")
# #
# dbcon = _sqlite3.connect('moncafe.db')
# with dbcon:
#     cursor = dbcon.cursor()
from persistence import *

def inserttodb(line):
    seperated = line.split(', ')
    what = seperated[0]
    if what == 'C':  # coffee stand
        repo.Coffee_stands.insert(Coffee_stands(*seperated[1:]))
    if what == 'S':  # Suppliers
        repo.Supplier.insert(Suppliers(*seperated[1:]))
    if what == 'E':  # Employees
        repo.Employees.insert(Employees(*seperated[1:]))
    if what == 'P':  # Products
        quan = 0
        if len(seperated) == 5 :
            quan = seperated[4]
        repo.Products.insert(Products(*seperated[1:], quan))
    # splited = line.split(",")
    # what = splited[0]
    # with dbcon:
    #     cursor = dbcon.cursor()
    #     if what == 'C':  # coffee stand
    #         converted = (int(splited[1]), splited[2], int(splited[3]))
    #         cursor.execute("INSERT INTO Coffee_stands values(?,?,?)", converted[0:])  # insert to Coffee stand
    #
    #     if what == 'S':  # Suppliers
    #         converted = (int(splited[1]), splited[2], splited[3])
    #         cursor.execute("INSERT INTO Suppliers values(?,?,?)", converted[0:])  # insert to Coffee stand
    #
    #     if what == 'E':  # Employees
    #         converted = (int(splited[1]), splited[2], splited[3], int(splited[4]))
    #         cursor.execute("INSERT INTO Employees values(?,?,?,?)", converted[0:])  # insert to Coffee stand
    #
    #     if what == 'P':  # Products
    #         quantity = 0
    #         if len(splited) == 5:
    #             quantity = int(splited[4])
    #         converted = (int(splited[1].strip()), splited[2].strip(), float(splited[3].strip()), quantity)
    #         cursor.execute("""INSERT INTO Products VALUES(?,?,?,?)""", converted[0:])  # insert to Coffee stand


# def createtables():
#     cursor.execute("""CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY,
#                                                 location TEXT NOT NULL,
#                                                 number_of_employees INTEGER)""")
#
#     cursor.execute("""CREATE TABLE Suppliers(id INTEGER PRIMARY KEY,
#                                             name TEXT NOT NULL,
#                                             contact_information TEXT)""")
#
#     cursor.execute("""CREATE TABLE Employees(id INTEGER PRIMARY KEY,
#                                             name TEXT NOT NULL,
#                                             salary REAL NOT NULL,
#                                             coffee_stand INTEGER REFERENCES Coffee_stand(id))""")
#
#     cursor.execute("""CREATE TABLE Products(id INTEGER PRIMARY KEY,
#                                                description TEXT NOT NULL,
#                                                price REAL NOT NULL,
#                                                quantity INTEGER NOT NULL)""")
#
#     cursor.execute("""CREATE TABLE Activities(product_id INTEGER REFERENCES Products(id),
#                                                quantity INTEGER NOT NULL,
#                                                activator_id INTEGER NOT NULL,
#                                                date DATE NOT NULL)""")


def main(args):
    # _sqlite3.connect('moncafe.db')
    # repo._start()
    repo.createtables()
    config = args[1]
    with open(config) as inputfile:
        for line in inputfile:
            inserttodb(line.strip())


if __name__ == '__main__':
    main(sys.argv)
