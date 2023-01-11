"""Write a function to return a list of even numbers.
The size of the list is to be given as an argument to the function
"""
import random
def even_num_list (length):
    list = []
    even_list = []

    limit = length * 5
    for num1 in range (1, limit):
        list.append (num1)
    for num2 in range (0, len (list)):
      if (list [num2] % 2) == 0:
        #for generating odd numbers change (==) to (!=)
        even_list.append (list [num2])
        if len (even_list) > (length - 1):
          break
    return even_list
length = eval (input ("enter the length of the list: "))
print ("the even list is: ", even_num_list (length))