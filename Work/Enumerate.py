import sys
import csv
def inventory_cost(filename):
    with open(filename, 'rt') as FH:
        rows = csv.reader(FH)  # using ssv.reader method to read the lines..no need of split
        headers = next(rows)
        total = 0.0
        for row_num, row in enumerate(rows,start=1):
            # print(line)
            try:
                val = int(row[1]) * float(row[2])
                total += val
            except ValueError:
                     print(f"Row{row_num}:Couldn't convert{row}")
        return total

cost = inventory_cost('missing.csv')
print("The total amount of the Products is ", cost)
