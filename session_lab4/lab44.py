"""Create a module named average with the following functionality:
A function that computes the average of numerical values in the list
Code to seek user input of 4 values and call the above function and print the average computed.
 Use for loop and append method of list class. ( use range() function to iterate a fixed number of times )
"""
import lab41.geomentry.average
list = [1, 2, 3, 4, 5]
print ("the average of list: ", lab41.geomentry.average.aveg_list (list))

print ("enter the 4 list values: ")
list_2 = []

for number in range (0, 4):
    value = input ()
    list_2.append (eval (value))
print ("the average of user list: ", lab41.geomentry.average.aveg_list (list_2))
