"""Read up about a Python package named "pandas" and
repeat the above exercise1 using pandas.
Locate the primary documentation for pandas and use it.
"""


import pandas as pd

f = pd.read_csv("Traffic_Violations.csv")
#C:\Users\Vedhavishwa\Downloads\Traffic_Violations.csv


#pd.options.display.max_rows = 1
genders=f['Gender']
#print(genders)
male_count=0
female_count=0

for details in genders:

    
    #gender = details['Gender']
    if details=='M':
        male_count+=1
    else:
        female_count+=1


print("The number of male and female drivers involved in traffic violations are {} males and {} females.".format(male_count,female_count))
