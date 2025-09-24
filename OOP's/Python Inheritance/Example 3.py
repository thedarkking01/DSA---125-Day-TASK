class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines.")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

p1 = Polygon([3, 4, 5])
p1.display_info()
perimeter = p1.get_perimeter()
print(f'Perimeter: {perimeter}')