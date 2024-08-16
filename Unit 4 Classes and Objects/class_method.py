class ExampleClass: 
    class_variable = 10

    @classmethod 
    def class_method(cls): 
        print(f"Class method called with class_variable: {cls.class_variable}")

# Call the class method
ExampleClass.class_method() # Output: "Class method called with class_variable: 10"

# often used when a variable is a constant

# Class methods are methods that are bound to the class itself rather than the instance/object. 
# They can access class-level attributes using (cls.) not self and perform operations related to the class as a whole. 
# Class methods are defined using the @classmethod decorator. 

# The class_method() is a class method defined within the ExampleClass class. 
# It can access the class-level attribute class_variable using cls.class_variable. 
# Class methods are typically used for operations that involve the class as a whole, such as alternative constructors or operations on class-level data.

