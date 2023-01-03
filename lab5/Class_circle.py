class Circle(object):

    def __init__(self,radius):
        self.radius=radius



        # pie*(r*r)
    def get_area(self):
        radius=self.radius
        pi = 3.14
        area = pi * (radius * radius)
        return "area of the circle is {}".format(area)

    # 2*pi*(r*r)

    def get_circle_circumference(self):
        radius=self.radius
        pi = 3.14
        circumference = 2 * pi * (radius * radius)
        return "circumference of the circle is {}".format(circumference)

    def __str__(self):

        return "the radius of the circle is {} ".format(self.radius)
