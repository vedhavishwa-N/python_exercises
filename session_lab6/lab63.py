import csv

filename = "100b.csv"
fields = []
rows = []
with open( filename, 'r') as file1:
    data = csv.reader (file1)
    fields = next (data)
    for row in data:
        rows.append (row)
 # get total number of rows
for row in rows:
    print ("book title- ", row [1])

