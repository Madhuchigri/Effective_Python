import csv
def read_inventory(filename):
    with open(filename, 'rt') as FH:
        rows = csv.reader(FH)  # using ssv.reader method to read the lines..no need of split
        headers = next(rows)
        product = []
        for row in rows:
            prod = {'name':row[0], 'quant':int(row[1]), 'price':float(row[2])}
            product.append(prod)
        return product

filename = "inventory.csv"

report = read_inventory(filename)
print(report)