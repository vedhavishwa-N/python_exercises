pi = 3.14
#formula=pie*(r*r)
def get_circle_area (radius):
    if radius.isdigit ():
        radius = eval (radius)
        area = pi * (radius * radius)
        return area
    else:
        print ("enter a valid input")

#formula=2*pi*(r*r)

def get_circle_circumference (radius):
    if radius.isdigit ():
        radius = eval (radius)
        circumference = 2 * pi * (radius * radius)
        return circumference
    else:
        print ("enter a valid input")