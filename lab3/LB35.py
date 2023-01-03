"""Write a function that returns a list of random integers.
 The length of list is to be provided as an argument
"""
import random

list=[]
def list_random_numbers(length):
    for numbers in range(0, length):
        list.append(random.randint(1, 1000))
    return list

print("enter the length of list :")
length=eval(input())
print("the list is: ",list_random_numbers(length))
