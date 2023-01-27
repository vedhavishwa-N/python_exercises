import csv
import Class_book

filename = "100b.csv"

fields = []
rows = []
with open (filename, 'r') as file1:
    data = csv.reader (file1)

    fields = next (data)

    for row in data:

        rows.append (row)

num = 1
for row in rows:

    a = row [0]
    b = row [1]
    c = row [2]
    d = row [3]
    e = row [4]
    f = row [5]
    g = row [6]
    h = row [7]


    OBJECT=Class_book.Book (a, b, c, d, e, f, g, h)
    print ("""object - {} - 
          {} """.format (num, OBJECT), '\n')
    num = num +1

