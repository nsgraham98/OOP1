num1 = float(input("Enter the first number: "))
operation = input("Enter either  'add', 'subtract', 'multiply', or 'divide': ")
num2 = float(input("Enter the second number: "))

if operation == "add":
    print(num1 + num2)
elif operation == "subtract":
    print(num1 - num2)
elif operation == "multiply":
    print(num1 * num2)
elif operation == "divide":
    print(num1 / num2)
else:
    print("Please enter a valid operation")
