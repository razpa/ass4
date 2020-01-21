import _sqlite3
import sys
from persistence import repo

def main():
    dbcon = _sqlite3.connect('moncafe.db')
    cur = dbcon.cursor()
    cur2 = dbcon.cursor()

    # ------ Print Tables ---------
    # print Activities
    cur.execute("""
        SELECT * FROM Activities ORDER BY date ASC""")

    print('Activities')
    for row in cur.fetchall():
        print(row)

    # print Coffee_stands
    cur.execute("""
        SELECT * FROM Coffee_stands ORDER BY id ASC""")

    print('Coffee stands')
    for row in cur.fetchall():
        print(row)

    # print Employees
    cur.execute("""
        SELECT * FROM Employees ORDER BY id ASC""")

    print('Employees')
    for row in cur.fetchall():
        print(row)

    # print Products
    cur.execute("""
        SELECT * FROM Products ORDER BY id ASC""")

    print('Products')
    for row in cur.fetchall():
        print(row)

    # print Suppliers
    cur.execute("""
        SELECT * FROM Suppliers ORDER BY id ASC""")

    print('Suppliers')
    for row in cur.fetchall():
        print(row)

    # ------ Print Employees Report ---------
    print("\n" + "Employees report")
    cur.execute("""
        SELECT
        Employees.id, Employees.name, Employees.salary, 
        Coffee_stands.location
        FROM Employees 
        JOIN Coffee_stands 
        ON Employees.coffee_stand = Coffee_stands.id
        ORDER BY Employees.name ASC
        """)

    for row in cur.fetchall():
        sum = 0
        for i in repo.Activities.find(row[0]):
            sum +=repo.Products.find(i.product_id).price
        print(*row[1:], sum)

    # ------ Print Actvity Report ---------
    print("\n" + "Activities")
    cur.execute("""
        SELECT
        Activities.date, Products.description, Activities.quantity, Employees.name, Suppliers.name
        FROM Activities 
            INNER JOIN Products
                ON Activities.product_id = Products.id
            LEFT JOIN Employees
                ON Activities.activator_id = Employees.id
            LEFT JOIN Suppliers
                ON Activities.activator_id = Suppliers.id
        ORDER BY Activities.date ASC
        """)
    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    main()
