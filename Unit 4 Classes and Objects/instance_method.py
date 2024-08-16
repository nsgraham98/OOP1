class ExampleClass:
    def __init__(self, value):
        self.value = value
    def instance_method(self):
        print(f"Instance method called with value: {self.value}")

# Create an object of MyClass
obj = ExampleClass(42)
# Call the instance method
obj.instance_method() # Output: "Instance method called with value: 42"

# instance_method(self) is a instance, requires an obj to work4
# self.value is static variable
# anything with self will be instance

# Instance methods are the most common type of methods in Python classes. 
# They are bound to the object/instance of the class and have access to the instance's attributes and other instance methods.

# In this example: 
# The instance_method() is an instance method defined within the ExampleClass class. 
# It can access the value attribute of the instance using self.value.

