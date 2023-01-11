"""Analyse Traffic Violation data you have in the file Traffic_Violations.csv
 ( https://drive.google.com/file/d/1lkVSOwYLop0n97hzEVUd0sqvX0PqEr4g/view?usp=sharing  .
  This is a zip file. Please unzip the file to obtain the CSV file. This is a very large file.
    ( Please note that this need not be done in python. It is adequate if you get this file by manually
     downloading from google drive )

Write a python script to process the downloaded and
uncompressed CSV file and compute
and print the number of male and female drivers involved in traffic violations.
"""
import csv
f = open("Traffic_Violations.csv", "r", encoding="utf8")


database = csv.DictReader(f)
male_count=0
female_count=0 


for details in database:
    # print(details)
    gender = details['Gender']
    if gender=='M':
        male_count+=1
    else:
        female_count+=1


print("The number of male and female drivers involved in traffic violations are {} males and {} females.".format(male_count,female_count))




