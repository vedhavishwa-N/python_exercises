class Rectangle(object):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    # AREA OF RECTANGLE =LENGTH*BRETH
    def get_area_rectangle(self):
        length=self.length
        width=self.width
        area = length * width
        return "area of the rectangle is {}".format(area)

    # perimeter=2(length*breth)
    def get_perimeter_rectangle(self):
        length=self.length
        width=self.width
        perimeter = 2 * (length + width)
        return "perimeter of the rectangle is {}".format(perimeter)

    def __str__(self):
        return "the rectangle length is {} and width is {}".format(self.length,self.width)




