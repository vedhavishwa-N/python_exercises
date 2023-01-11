"""Write a function that returns a list of random integers.
 The length of list is to be provided as an argument
"""
import random


def list_random_numbers (length):
    list = []
    limit = length * 5
    for numbers in range (0, length):
        list.append (random.randint (1, limit))
    return list

length = eval (input ("enter the length of list : "))
print ( "the list is: ", list_random_numbers (length))
