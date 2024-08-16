class Student:
    __profession = "student" #private static attribute
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def get_email (self):
        return self.email
    def updateAge(self, newAge):
        self.age = newAge
    def study (self):
        print (self.name + " is studying")
    def getInfo(self):
        print("Name: " + self.name + " Age: " + str(self.age) + " Email: " + self.email);
    @staticmethod #static method 
    def getProfession():
        return Student.__profession
    
john = Student("John Nelson", 31, "john@sait.ca")

print (john.getProfession()) #invoke static method <- CAN access __profession
# print (john.__profession) #private attribute <- CANNOT access __profession
