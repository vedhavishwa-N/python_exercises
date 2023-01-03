"""Modify the above module to keep the size of the list of values flexible.
Use a while loop to allow the user to enter any number of values.
"""
import lab41.geomentry.average
l=[]
print("enter the number of values: ")
num=eval(input())
print("enter the values: ")
dummy=0
while dummy < num:
    dummy=dummy+1
    l.append(eval(input()))
print("the list is ",l)
print("the average of list",lab41.geomentry.average.aveg_list(l))