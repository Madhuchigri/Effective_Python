import csv


def parse_csv(filename):
    """ This Funtion Takes the CSV file and returns list of Dictonaries"""
    with open(filename) as FH:
        rows = csv.reader(FH)
        # Read the headers
        headers = next(rows)
        records = []
        for row in rows:
            if not rows:
                continue
            record = dict(zip(headers,row))
            records.append(record)
    return records
