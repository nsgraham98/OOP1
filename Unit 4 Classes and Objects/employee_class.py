class Employee:

    def __init__(self, name="", hours_worked=0, rate_of_pay=0):
        self.__name= name
        self.__hours = float(hours_worked)
        self.__pay = float(rate_of_pay)

    def get_name(self):
        return self.__name
    def get_hours_worked(self):
        return self.__hours
    def get_rate_of_pay(self):
        return self.__pay
    
    def set_name(self, name):
        self.__name = name
    def set_hours_worked(self, hours):
        self.__hours = float(hours)
    def set_rate_of_pay(self, rate_of_pay):
        self.__pay = float(rate_of_pay)

    def __str__(self):
        return f"Name: {self.__name}\nHours: {self.__hours} Rate: {self.__pay:.2f}\nGross Pay: {self.calc_gross_pay():.2f}\n"

    def add_hours_worked(self, hours_worked):
        self.__hours += hours_worked

    def calc_gross_pay(self):
        gross_pay = self.__hours * self.__pay
        return gross_pay