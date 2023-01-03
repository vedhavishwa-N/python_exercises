"""Write a function to compute and return the mode
for the values contained in the given list ( https://en.wikipedia.org/wiki/Mode_(statistics) )
"""
import statistics
list=[1,2,3,4,5,6,7,9,8,9]
print("mode of the list computer generated",statistics.mode(list))
max=0
result=0
for num in list:
    if max < (list.count(num)):
        max=list.count(num)
        result=num

print("the mode of list is ",result)




