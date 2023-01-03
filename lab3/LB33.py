"""Write a function to compute and return the median for the values
contained in the given list. ( https://en.wikipedia.org/wiki/Median )
"""

median=0
list=[1,2,3,4,5,6,7,8,9,10,4,5,6,7,8]
s_list=sorted(list)
print("values of the list",s_list)
if len(list)%2==0:
    pos1=int(len(s_list)/2)
    pos2=pos1-1
    median=(s_list[pos1]+s_list[pos2])/2
else:
    pos3=int(((len(s_list)+1)/2)-1)
    median=s_list[pos3]

print("the mean value is ",median)