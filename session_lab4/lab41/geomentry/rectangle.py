#AREA OF RECTANGLE =LENGTH*BRETH
def get_area_rectangle (length, breadth):
    if length.isdigit and breadth.isdigit ():
     length = eval (length)
     breadth = eval (breadth)
     area = length * breadth
     return area
    else:
        print ("enter a valid input")
#perimeter=2(length*breth)
def get_perimeter_rectangle (length, breadth):
    if length.isdigit and breadth.isdigit ():
        length = eval (length)
        breadth = eval (breadth)
        perimeter = 2 * (length + breadth)
        return perimeter
    else:
        print ("enter a valid input")
