def inventory_cost(filename):
    with open(filename) as FH:
        headers = next(FH)
        total = 0.0
        for line in FH:
            # print(line)
            parts = line.split(',')
            val = int(parts[1]) * float(parts[2])
            total += val
        return total


cost = inventory_cost("inventory.csv")
print("The total amount of the Products is ", cost)
