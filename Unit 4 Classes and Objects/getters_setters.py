# get-ers and set-ers are used to access private members (get = read attribute), (set = update atttribute)

class Person:
    def __init__(self, person_name, person_age):
        self.__name = person_name
        self.__age = person_age
    def get_name (self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age (self):
        return self.__age
    def set_age(self, age):
        self.__age = age

p = Person('Maria', 36)
print(p.get_name( ), ",", p.get_age())

p.set_name("Mary")
p.set_age(25)
print (p.get_name( ), ",", p.get_age())
