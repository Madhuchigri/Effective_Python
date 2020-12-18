import sys
import csv
def inventory_cost(filename):
    with open(filename, 'rt') as FH:
        rows = csv.reader(FH)  # using ssv.reader method to read the lines..no need of split
        headers = next(rows)
        total = 0.0
        for row in rows:
            # print(line)
            try:
                val = int(row[1]) * float(row[2])
                total += val
            except ValueError:
                    for Badrow, row in enumerate(FH):
                        print("got invalid row", Badrow,row)
        return total

cost = inventory_cost('missing.csv')
print("The total amount of the Products is ", cost)