num1 = int(input("enter the first integer: "))
num2 = int(input("enter the second integer: "))

if num1 % num2 == 0:
    print(num1, "is a multiple of ", num2)
else:
    print(num1, "is not a multiple of ", num2)