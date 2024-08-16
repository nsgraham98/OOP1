
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

operation = input("Enter the operation (add, subtract, multiply, divide) you'd like to perform: ")

if operation == "add":
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == "subtract":
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == "multiply":
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == "divide":
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid operation input")
    

