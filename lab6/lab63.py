import csv

filename = "100books.csv - Copy of 100books.csv.csv"
fields = []
rows = []
with open(filename, 'r') as file1:
    r = csv.reader(file1)
    fields = next(r)
    for row in r:
        rows.append(row)
 # get total number of rows
for row in rows:
    print("book title- ",row[1])

