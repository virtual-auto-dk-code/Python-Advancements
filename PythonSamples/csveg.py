import csv
# file = open("./Sample.csv")
# csvreader = csv.reader(file)
# header = next(csvreader)
#print(header)

with open('./Sample.csv', encoding='latin-1') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    # Continue processing the CSV file...
    rows = []
    for row in csvreader:
        rows.append(row)
    print(rows)
    file.close()