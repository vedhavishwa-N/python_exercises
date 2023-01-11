"""Circle
Write a function to compute and return the area of a circle
Write a function to compute and return the circumference of a circle
"""
def area_of_circle (radius_of_circle):
    #area of circle is pi radius square
    pi = 3.14
    area = pi * (radius_of_circle * radius_of_circle)
    return area

def circumference_of_circle (radius_of_circle):
    #circumference of circle is two pi radius 
    pi = 3.14
    circumference = 2 * pi * radius_of_circle
    return circumference

#test cases

radius = 4
print ("\nthe area of circle with radius {} is {}".format (radius, area_of_circle (radius)))
print ("\nthe circumference of circle with radius {} is {}".format (radius, circumference_of_circle (radius)))
