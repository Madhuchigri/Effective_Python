import csv


def parse_csv(filename,select=None,types=[str,int]):
    with open(filename) as FH:
        rows = csv.reader(FH)
        # Read the headers
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not rows:
                continue
            if select:
                row = [[row[index] for index in indices]]
            if types:
                row = [func(val) for func,val in zip(types,row)]
            record = dict(zip(headers,row))
            records.append(record)
    return records
