class Student:
    def __init__(self, name="", id=0, address=""):
        self.__name = name
        self.__id = int(id)
        self.__address = address

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_address(self):
        return self.__address
    
    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f"Name: {self.__name}\nID: {self.__id}\nAddress: {self.__address}\n"
    
# my_info = Student("Nick Graham", 956736, "123 Street St.")
# print(my_info)


class Circle:
    def __init__(self, radius=0):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def get_circle_area(self, radius):
        self.__circle_area = 3.14 * (radius**2)
        return self.__circle_area 
      
    def get_circle_perimeter(self, radius):
        self.__circle_perimeter = radius * 2 * 3.14
        return self.__circle_perimeter
    
    def set_circle_radius(self, radius):
        self.__radius = radius

    
    def display_circle_perimeter(self, radius):
        self.__radius = radius
        print(f"For circle with radius = {self.__radius} units:\nPerimeter = {self.get_circle_perimeter(self.__radius):.2f} units\n")

    def display_circle_area(self, radius):
        self.__radius = radius
        print(f"For circle with radius = {self.__radius} units:\nArea = {self.get_circle_area(self.__radius):.2f} units^2\n")
    
    def __str__(self):
        return f"For circle with radius = {self.__radius} units:\nArea = {self.get_circle_area(self.__radius)} units^2\nPerimeter = {self.get_circle_perimeter(self.__radius)} units"

# my_circle = Circle()
# my_circle.display_circle_perimeter(5)
# my_circle.display_circle_area(5)

class BankAccount:
    def __init__(self, account_number=0, customer_name="", balance=0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance
    
    def get_account_number(self):
        return self.__account_number
    def get_customer_name(self):
        return self.__customer_name
    def get_balance(self):
        return self.__balance
    
    def set_account_number(self, account_number):
        self.__account_number = account_number
    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name
    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self):
        deposit_amount = float(input("How much money would you like to deposit? $"))
        self.__balance += deposit_amount
        print("Deposit Successful.\n")
        self.display()
    
    def withdraw(self):
        withdraw_amount = float(input("How much money would you like to withdraw? $"))
        self.__balance -= withdraw_amount
        print(f"Withdrawl successful.\n")
        self.display()

    def display(self):
        print(f"Account information:\nCustomer Name: {" "*2}{self.__customer_name}\nAccount Number:{" "*2}#{self.__account_number}\nAccount balance: ${self.__balance}")

customer = BankAccount()

customer.set_account_number(123)
customer.set_customer_name("Nick Graham")
customer.set_balance(100)

customer.deposit()

customer.withdraw()

        