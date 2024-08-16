from employee_class import Employee
 
def main():
    # Test constructor
    emp1 = Employee()
    emp2 = Employee("Harvey", 0, 11.20)
    
    # Test setters
    emp1.set_name("Sara")
    emp1.set_hours_worked(40)
    emp1.set_rate_of_pay(15)
    
    # Test getters
    print("Payroll Report for", emp1.get_name())
    print("Hours =", emp1.get_hours_worked())
    print("Rate =", emp1.get_rate_of_pay())
    
    # Test calc_gross_pay() method
    print("Gross Pay = $", emp1.calc_gross_pay(), sep='')
    print()
    
    # Test add_hours_worked()
    emp2.add_hours_worked(10)
    emp2.add_hours_worked(5)
    print("Payroll Report for " + emp2.get_name())
    
    # Test of __str__()
    print(emp2)
 
main()
 