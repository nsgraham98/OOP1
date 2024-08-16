class Person:
    def __init__(self, person_name, person_age):
        self.__name = person_name
        self.__age = person_age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, person_name):
        self.__name = person_name

    def set_age(self, person_age):
        self.__age = person_age

    def __str__ (self):
        return f"Name is {self.__name}, age is {self.__age}"
    
def main ():
    p = Person('Dave', 35)
    print (p)
    print (p.get_age())
    print (p.get_name())
# change the age
    p.set_age(61)
    print(p)

main()