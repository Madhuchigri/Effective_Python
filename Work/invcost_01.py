def inventory():
    with open("Data/inventory.csv") as FH:
        headers = next(FH)
        total = 0.0
        for line in FH:
           # print(line)
            parts = line.split(',')
            val = int(parts[1]) * float(parts[2])
            total += val
        print("The total amount of the inventory is", total)

inventory()
