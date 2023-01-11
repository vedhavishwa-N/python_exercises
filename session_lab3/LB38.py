"""Write a function to do the following:
-A list of distances in miles will be provided as an argument
-The function should return a list containing the same values converted to Kilometers
"""
#miles to kilometer is miles*1.609
kilometer_list = []
def distance_convert (list):
    for value in list:
        kilometer_list.append (value * 1.609)
    return kilometer_list
print ("enter the distance vales for  miles list with comma : ")
miles_list = list (eval (input()))
print( "the kilometers list is : ", distance_convert (miles_list))