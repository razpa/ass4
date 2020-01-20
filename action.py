import _sqlite3
import sys
from datetime import datetime
from persistence import *

import printdb





def main(args):
    input = args[1]
    print(input)
    with open(input) as activities:
        for line in activities:
            print(line)
            activate(line)
    # printdb.main()


# def activate(line):
#     separated = line.split(", ")
#     product_id = int(separated[0])
#     dbcon = _sqlite3.connect('moncafe.db')
#     with dbcon:
#         cursor = dbcon.cursor()
#         cursor.execute("SELECT quantity FROM Products WHERE id=?", [product_id]) #
#         qun = cursor.fetchone()
#         new_quantity = qun[0] + int(separated[1])
#         converted = (int(separated[0]), int(separated[1]), int(separated[2]), separated[3]) #int(datetime.datetime.fromtimestamp(separated[3]).strftime('%Y-%m-%d %H:%M:%S')))
#         if int(separated[1]) < 0:
#             if new_quantity > 0:
#                 cursor.execute("UPDATE Products SET quantity=? WHERE id=?", (new_quantity, product_id))
#                 cursor.execute("INSERT INTO Activities values(?,?,?,?)", converted[0:])  # insert to Coffee stand
#         if int(separated[1]) > 0:
#             cursor.execute("UPDATE Products SET quantity=? WHERE id=?", (new_quantity, product_id))
#             cursor.execute("INSERT INTO Activities values(?,?,?,?)", converted[0:])  # insert to Coffee stand
def activate(separated):
    product = repo.Products.find(separated[0])
    new_quantity = product.quantity + int(separated[1])
    if  new_quantity > 0 or product.quantity > 0:
        repo.Products.update_quantity(product.id, new_quantity)
        repo.Activities.insert(Activities(separated))


if __name__ == '__main__':
    main(sys.argv)
