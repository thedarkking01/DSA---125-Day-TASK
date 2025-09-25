# Replace ___ with your code

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

# create the Quadrilateral class
class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges.")
# create an object of Quadrilateral
Quad=Quadrilateral([1,4,5,6])

# call the display_info() method using the object
Quad.display_info()