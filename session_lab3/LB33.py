"""Write a function to compute and return the median for the values
contained in the given list. ( https://en.wikipedia.org/wiki/Median )
"""

list= [ 1, 2, 3, 4, 5, 6]

print ("values of the list", list)
def compute_median (list):
    sorted_list = sorted (list)
    if len (list) % 2 == 0:
        position_1 = int (len (sorted_list) / 2)
        position_2 = position_1 - 1
        median = (sorted_list [position_1] + sorted_list [position_2] ) / 2
    else:
        position = int ((( len (sorted_list) + 1) / 2) - 1)
        median = sorted_list [position]
    return "The meandian value is {}".format (median)

print (compute_median (list))