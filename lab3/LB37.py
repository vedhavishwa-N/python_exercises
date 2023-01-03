"""Write a function to return a list of even numbers.
The size of the list is to be given as an argument to the function
"""
import random
list=[]
even_list=[]
def even_num_list(length):
    for num1 in range(1, 10000):
        list.append(num1)
    for num2 in range(0,len(list)):
      if (list[num2]%2)==0:
        #for generating odd numbers change (==) to (!=)
        even_list.append(list[num2])
        if len(even_list)>(length-1):
          break
    return even_list
print("enter the length of the list: " )
length=eval(input())
print("the even list is: ", even_num_list(length))