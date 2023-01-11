"""Extend the above function to also receive 2 additional optional arguments - min and max
to indicate the min and max values of the members of the list.
"""
import random


def list_random_number (length, min, max):
  list = []  
  for num in range (0, length):
    if max != "" and min != "":
      min = int (min)
      max = int (max)
      list.append (random.randint (min, max))
    else:
      list.append (random.randint (min, max))
  return list

length = eval (input ("enter the length of list : "))
print ("enter the max and min values of the list: ")
max_of_list = input()
min_of_list = input()
print ("the list is: ", list_random_number (length, min_of_list, max_of_list))
