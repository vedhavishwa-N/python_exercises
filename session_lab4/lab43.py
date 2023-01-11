"""Modify the module related to exercise1 above to ensure
that non-numeric data is not provided as arguments and
again test using module related to exercise2.
"""
import lab41.geomentry.circle
import lab41.geomentry.rectangle
print ("enter the radius of circle: ")
r = input ()
print ("enter length and breadth: ")
l = input ()
b = input ()

print ("the area of circle", lab41.geomentry.circle.get_circle_area (r))
print ("circumference of circle", lab41.geomentry.circle.get_circle_circumference (r))
print ("area of rectangle", lab41.geomentry.rectangle.get_area_rectangle (l, b))
print ("perimeter of rectangle", lab41.geomentry.rectangle.get_perimeter_rectangle (l, b))
