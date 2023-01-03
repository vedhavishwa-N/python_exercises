"""Test the Circle class and methods by creating 100 circle objects with varying values for radius.
Use a for loop and 'random' module to generate the tests. """
import lab5.Class_circle
import random
for num in range(1,101):
    radius=random.randint(1,100)
    circle=lab5.Class_circle.Circle(radius)
    print("----------",num,"----------------")

    print(circle)
    print(circle.get_area())
    print(circle.get_circle_circumference())

    print("________________________________")
