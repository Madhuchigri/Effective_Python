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



def read_prices(filename1):
    with open(filename1, 'rt') as FH:
        prices = dict()
        rows = csv.reader(FH)  # using ssv.reader method to read the lines..no need of split
        for row in rows:
           try:
            prices[row[0]] = float(row[1])
           except IndexError:
               continue   # Empty row found so continuing with the execution
    return prices


def make_report(product,prices):
    values = list()
    for prod in product:
        name = prod['name']
        quant = prod['quant']
        price = prod['price']
        latest_price = prices[name]
        values.append ((name,quant,latest_price,latest_price-price))
    return values

filename = "inventory.csv"
filename1 = "prices.csv"

report = read_inventory(filename)
price_file = read_prices(filename1)
report1 = make_report(report,price_file)
print(report1)
