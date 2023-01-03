"""Write a function to do the following:
-Take a list containing temperatures in fahrenheit
-The function should return a list containing the temperature in Celsius.
"""
#fahrenheit to celsius is fahrenheit*1.609
celsius_list=[]
def temperature_convert(list):
    for value in list:
        celsius_list.append((value-32)*5/9)
    return celsius_list
print("enter the distance vales(fahrenheight) for  temperatue list with comma : ")
fahrenheit_list=list(eval(input()))
print("the list of temperature in celsius: ",temperature_convert(fahrenheit_list))