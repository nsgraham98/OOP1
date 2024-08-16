class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_email(self):
        return self.email
    
    def set_age(self, new_age):
        self.age = new_age

    def study(self):
        return f"{self.name} is studying"
    
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"
    
john = Student("John", 25, "john.johnson@edu.sait.ca")
print(john.get_info())

john.set_age(18)
print(john.get_info())

steve = Student("Steve", 21, "steve.stevenson@edu.sait.ca")
print(steve.get_info())

mike = Student("Mike", 30, "mike.michaels@edu.sait.ca")
print(mike.get_email())




# print(john.name)
# print(john.age)
# print(john.email)

# print(steve.name)
# print(steve.age)
# print(steve.email)

# print(mike.name)
# print(mike.age)
# print(mike.email)

