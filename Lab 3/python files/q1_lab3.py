num_1 = int(input("Enter the first integer: "))
num_2 = int(input("Enter the second integer: "))

if num_1 > num_2:
    print(num_1, "is larger than", num_2)
elif num_2 > num_1:
    print(num_2, "is larger than", num_1)
else:
    print("These numbers are equal")