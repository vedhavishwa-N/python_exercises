"""Test the class and methods by creating 100 rectangle objects
with varying values for length and breadth. Use a for loop and random module to generate the tests.

"""
import Class_rectangle
import random
for num in range (1, 101):
    length = random.randint (100, 200)
    width = random.randint (10, 100)
    rect = Class_rectangle.Rectangle (length, width)
    print ("----------",num,"----------------")

    print (rect)
    print (rect.get_area_rectangle ())
    print (rect.get_perimeter_rectangle ())

    print("________________________________")
