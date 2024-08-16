from person import Person
def print_person_list():
    person_list = []
    name = input("Please enter a name ('quit' to exit program): ")
    while name != "quit":
        age = input(f"Please enter {name}'s age: ")
        p = Person(name, age)
        person_list.append(p)
        name = input("Please another enter a name ('quit' to exit program): ")
    for person in person_list:
        print(person)

print_person_list()