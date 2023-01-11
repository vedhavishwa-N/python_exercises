"""Write a separate module named tests which should contain code to test the functions
 from the circle and rectangle modules with a fixed set of values (no user input required)"""
import session_lab4.lab41.geomentry.circle
import session_lab4.lab41.geomentry.rectangle
r=5
l=4
b=2
print("area of circle", session_lab4.lab41.geomentry.circle.get_circle_area(r))
print("circumference of circle", session_lab4.lab41.geomentry.circle.get_circle_circumference(r))
print("area of rectangle", session_lab4.lab41.geomentry.rectangle.get_area_rectangle(l, b))
print("perimeter of rectangle", session_lab4.lab41.geomentry.rectangle.get_perimeter_rectangle(l, b))
