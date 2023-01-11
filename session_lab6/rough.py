# # importing csv module
# import csv

# # csv file name
# filename = "100books.csv - Copy of 100books.csv.csv"

# # initializing the titles and rows list
# fields = []
# rows = []

# # reading csv file
# with open(filename, 'r') as file1:
#     # creating a csv reader object
#     r = csv.reader(file1)

#     # extracting field names through first row
#     fields = next(r)

#     # extracting each data row one by one
#     for row in r:

#         rows.append(row)

#     # get total number of rows
#     print("Total no. of rows: {}".format ((r.line_num)))

# # printing the field names
# print('Field names are:' + ','.join(field for field in fields))

# # printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in rows[:5]:
#     # parsing each column of a row
#     for col in row:
#         print("%10s" % col, end=" "),
#     print('\n')

for i in  range(0,7):
    while i ==4:
        print("five")
        i=1
    while i==6:

        print("6")



