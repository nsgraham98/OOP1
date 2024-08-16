def rectangle_area_func(length, width):
    rectangle_area = length * width
    print(f"For a rectangle with:\nLength = {length:.2f}\nWidth = {width:.2f}\nArea = {rectangle_area:.2f}")
    return rectangle_area

rectangle_area_func(float(input("Enter the length of the rectangle you'd like to find the area of: ")), float(input("Enter the width of the rectangle you'd like to find the area of: ")))