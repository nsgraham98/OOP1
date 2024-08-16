grocery_list = []
grocery = input("Enter a grocery item (type 'quit' to exit): ")

while grocery != "quit": 
    grocery_list.append(grocery)
    grocery = input("Enter next grocery item: ")
    
print(f"Your grocery list: {grocery_list}")
    