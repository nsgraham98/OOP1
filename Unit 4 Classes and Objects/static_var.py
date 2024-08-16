class Person:

    count = 0 # initialize class variable

    def __init__(self, person_name, person_age):
        self.__name = person_name
        self.__age = person_age
        Person.count += 1 # increment class variable

    def get_count():
        return Person.count

print(Person.count, 'person objects created.') # Output: 0 person objects created.
person1 = Person("Sam", 30)
print(Person.count, 'person objects created.') # Output: 1 person objects created.
person2 = Person("Mike", 40)
print(Person.count, 'person objects created.') # Output: 2 person objects created.

# count is static variable - accessable from anywhere (not just within the class)
# changing count changes the value for ALL objecs

print(Person.get_count(), "person objects created.")