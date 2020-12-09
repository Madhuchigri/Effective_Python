import sys
import csv


def inventory_cost(filename):
    with open(filename, 'rt') as FH:
        rows = csv.reader(FH)  # using ssv.reader method to read the lines..no need of split 
        headers = next(rows)
        total = 0.0
        for row in rows:
            # print(line)
            val = int(row[1]) * float(row[2])
            total += val
        return total


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "inventory.csv"

cost = inventory_cost("inventory.csv")
print("The total amount of the Products is ", cost)