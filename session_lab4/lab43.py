"""Modify the module related to exercise1 above to ensure
that non-numeric data is not provided as arguments and
again test using module related to exercise2.
"""
import lab41.geomentry.circle
import lab41.geomentry.rectangle
print ("enter the radius of circle: ")
radius = input ()
print ("enter length and breadth: ")
length = input ()
breadth = input ()

print ("the area of circle", lab41.geomentry.circle.get_circle_area (radius))
print ("circumference of circle", lab41.geomentry.circle.get_circle_circumference (radius))
print ("area of rectangle", lab41.geomentry.rectangle.get_area_rectangle (length, breadth))
print ("perimeter of rectangle", lab41.geomentry.rectangle.get_perimeter_rectangle (length, breadth))
