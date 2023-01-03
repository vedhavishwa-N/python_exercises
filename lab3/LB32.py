"""Write a function to compute and return the arithmetic mean for the values contained
in the given list.(https://en.wikipedia.org/wiki/Mean)"""
import statistics
list=[1,2,3,4,5,6,7,8,9,10]
mean=0
sum=0
list=[1,2,3,4,5,6,7,8,9,10]

print("values of the list",list)
for num in list:
    sum=sum+num
mean=(sum/len(list))
print("the mean value is ",mean)
# using in built function
print("computer generated mean is ",statistics.mean(list))