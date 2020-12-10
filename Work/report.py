
import csv
def read_inventory(filename):
    with open(filename, 'rt') as FH:
        rows = csv.reader(FH)  # using ssv.reader method to read the lines..no need of split
        headers = next(rows)
        product = []
        for row in rows:
            prod = (row[0], int(row[1]), float(row[2]))
           # print(tuple1)
            product.append(prod)
        return product

filename = "inventory.csv"

report = read_inventory(filename)
print("Inventory products",report)
