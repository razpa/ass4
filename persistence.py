# file: persistence.py
import _sqlite3
import os
import sqlite3
import atexit


# Data Transfer Objects:
class Employees(object):
    def __init__(self, id, name, salary, coffee_stand):
        self.id = id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class Suppliers(object):
    def __init__(self, id, name, contact):
        self.id = id
        self.name = name
        self.contact_information = contact


class Products(object):
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity


class Coffee_stands(object):
    def __init__(self, id, location, num):
        self.id = id
        self.location = location
        self.number_of_employees = num


class Activities(object):
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date


# Data Access Objects:
# All of these are meant to be singletons
class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        with self._conn:
            self._conn.cursor().execute("""
               INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?,?,?,?)
           """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Employees WHERE id = ?
        """, [id])
        return Employees(*c.fetchone())


class _Supplier:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        with self._conn:
            self._conn.cursor().execute("""
                INSERT INTO Suppliers (id, name, contact_information) VALUES (?,?,?)
                """, [supplier.id, supplier.name, supplier.contact_information])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT * FROM Suppliers WHERE id = ?
                """, [id])
        return Suppliers(*c.fetchone())


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        with self._conn:
            self._conn.cursor().execute("""
                INSERT INTO Products (id, description, price, quantity) VALUES (?,?,?,?)
                """, [product.id, product.description, product.price, product.quantity])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT * FROM Products WHERE id = ?
                """, [id])
        return Products(*c.fetchone())

    def update_quantity(self, product_id, new_quantity):
        c = self._conn.cursor()
        c.execute("UPDATE Products SET quantity=? WHERE id=?", (new_quantity, product_id))


class _Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, stand):
        with self._conn:
            self._conn.cursor().execute("""
            INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)"""
                                        , [stand.id, stand.location, stand.number_of_employees])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Coffee_stands WHERE id = ?
            """, [id])
        return Coffee_stands(*c.fetchone())


class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activity):
        with self._conn:
            self._conn.cursor().execute("""
            INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
            """, [activity.product_id, activity.quantity, activity.activator_id, activity.date])

    def find(self, activitor_id):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Activities WHERE activator_id = ?
            """, [activitor_id])
        return [Activities(*row) for row in all]

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT * FROM Activities
            """).fetchall()
        return [Activities(*row) for row in all]


# The Repository
class _Repository(object):
    def __init__(self):
        self._conn = _sqlite3.connect('moncafe.db')
        self.Employees = _Employees(self._conn)
        self.Supplier = _Supplier(self._conn)
        self.Products = _Products(self._conn)
        self.Coffee_stands = _Coffee_stands(self._conn)
        self.Activities = _Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def _start(self):
        db_exist = os.path.isfile('moncafe.db')  # define databise
        if db_exist:
            os.remove('moncafe.db')  # delete database if exist
            self._conn = _sqlite3.connect('moncafe.db')

    def createtables(self):
        with self._conn:
            cursor = self._conn.cursor()
            cursor.executescript("""CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY,
                                                    location TEXT NOT NULL,
                                                    number_of_employees INTEGER);
                                    CREATE TABLE Suppliers(id INTEGER PRIMARY KEY,
                                                name TEXT NOT NULL,
                                                contact_information TEXT);
                                    CREATE TABLE Employees(id INTEGER PRIMARY KEY,
                                                name TEXT NOT NULL,
                                                salary REAL NOT NULL,
                                                coffee_stand INTEGER REFERENCES Coffee_stand(id));
                                    CREATE TABLE Products(id INTEGER PRIMARY KEY,
                                                   description TEXT NOT NULL,
                                                   price REAL NOT NULL,
                                                   quantity INTEGER NOT NULL);
                                    CREATE TABLE Activities(product_id INTEGER REFERENCES Products(id),
                                                   quantity INTEGER NOT NULL,
                                                   activator_id INTEGER NOT NULL,
                                                   date DATE NOT NULL);""")


# the repository singleton
repo = _Repository()
atexit.register(repo._close)
