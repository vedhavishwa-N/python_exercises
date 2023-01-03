#AREA OF RECTANGLE =LENGTH*BRETH
def get_area_rectangle(length,breth):
    if length.isdigit and breth.isdigit():
     length=eval(length)
     breth=eval(breth)
     area=length*breth
     return area
    else:
        print("enter a valid input")
#perimeter=2(length*breth)
def get_perimeter_rectangle(length,breth):
    if length.isdigit and breth.isdigit():
        length = eval(length)
        breth = eval(breth)
        perimeter=2*(length+breth)
        return perimeter
    else:
        print("enter a valid input")
