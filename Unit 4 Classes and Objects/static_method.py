class MathUtilitiesClass:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def mul(a, b):
        return a * b

# Call the static method
print(MathUtilitiesClass.add(2, 3)) # Output: 5
print(MathUtilitiesClass.mul(2, 3)) # Output: 6


# Static methods are methods that do not have access to instance-specific data or class-level data. 
# They are not bound to the instance or the class and behave like regular functions within the class. 
# Static methods are defined using the @staticmethod decorator. 

# In this example: 
# Define add() as a static method defined within the MathUtilitiesClass class. 
# It does not have access to any instance-specific or class-level data and operates purely on the arguments passed to it. 

