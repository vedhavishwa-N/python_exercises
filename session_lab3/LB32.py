"""Write a function to compute and return the arithmetic mean for the values contained
in the given list.(https://en.wikipedia.org/wiki/Mean)"""

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print ("values of the list", list)
def arithmetic_mean_for_list (list):
    mean = 0
    sum = 0
    for num in list:
        sum += num
    mean = (sum / len (list))
    return "The mean value is {}".format (mean)
print (arithmetic_mean_for_list (list))

# import statistics
# using in built function
# print("computer generated mean is ",statistics.mean(list))
