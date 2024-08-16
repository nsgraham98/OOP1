def circumference_func(radius):
    circumference = radius * 3.14 * 2
    print(f"For circle with radius = {radius}\nCircumference = {circumference:.2f}")
    return circumference

def circle_area_func(radius):
    circle_area = 3.14 * (radius**2)
    print(f"For circle with radius = {radius}\nArea = {circle_area:.2f}^2")
    return circle_area

circumference_func(float(input("Enter the radius to find the circumference of the circle: ")))
circle_area_func(float(input("Enter the radius to find the area of the circle: ")))
