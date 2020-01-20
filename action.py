import sys

import printdb
from persistence import repo, Activities


def main(args):
    input = args[1]
    with open(input) as activities:
        for line in activities:
            print(line)
            activate(line.split(", "))
    printdb.main()


def activate(seperated):
    product = repo.Products.find(seperated[0])
    new_quantity = product.quantity + int(seperated[1])
    if new_quantity > 0 or product.quantity > 0:
        repo.Products.update_quantity(product.id, new_quantity)
        repo.Activities.insert(Activities(*seperated))


if __name__ == '__main__':
    main(sys.argv)
