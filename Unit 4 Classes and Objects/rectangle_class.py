class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length
    
    def set_width(self, width_value):
        self.width = width_value

    def set_length(self, length_value):
        self.length = length_value
    
    def get_rectangle_area(self):
        return self.width * self.length
    
    def get_rectangle_perimeter(self):
        return self.width*2 + self.length*2
    
def main():
    width = float(input("Enter the width of the rectangle: "))

    length = float(input("Enter the length of the rectangle: "))

    my_rectangle = Rectangle(width, length)

    print(f"Area of the rectangle: {my_rectangle.get_rectangle_area()}")

    print(f"Perimeter of the rectangle: {my_rectangle.get_rectangle_perimeter()}")

main()