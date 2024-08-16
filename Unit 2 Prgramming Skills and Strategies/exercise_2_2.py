# volume = h * 3.14 * r^2
# area = 2 * 3.14 * r * h 

cylinder_height = input("What is the cylinder's height?")
cylinder_radius = input("What is the cylinder's radius?")

cylinder_height = float(cylinder_height)
cylinder_radius = float(cylinder_radius)

cylinder_volume = cylinder_height * 3.14 * cylinder_radius**2
cylinder_area = 2 * 3.14 * cylinder_radius * cylinder_height

print("Cylinder area:", cylinder_area)
print("Cylinder Volume:", cylinder_volume)