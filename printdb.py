import _sqlite3
import sys

if __name__ == '__main__':
    dbcon = _sqlite3.connect('moncafe.db')
    cur = dbcon.cursor()

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
    print("Employees report")
    # cur.execute("""
    #     SELECT emp.name, emp.salary, cs.location act.quantity
    #     FROM Employees as amp
    #     JOIN Coffee_stands as cs
    #     on emp.coffee_stand = cs.id
    #     JOIN Activities as act
    #     on emp.id = act.activator_id""")

    cur.execute("""
        SELECT
        Employees.name as name, Employees.salary as salary,
        Coffee_stands.location as location,
        Activities.quantity as num
        FROM
        Employees
        LEFT JOIN Employees.coffee_stand = Coffee_stands.id
        LEFT JOIN Employees.id = Activities.activator_id""")
