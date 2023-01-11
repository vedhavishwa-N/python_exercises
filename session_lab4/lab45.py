"""Modify the above module to keep the size of the list of values flexible.
Use a while loop to allow the user to enter any number of values.
"""
import lab41.geomentry.average
list = []
size = eval (input (" enter the number of values: "))
print ("enter the values: ")
dummy = 0
while dummy < size:
    dummy = dummy +1
    list.append (eval (input ()))
print ("the list is ", list)
print ("the average of list", lab41.geomentry.average.aveg_list (list))