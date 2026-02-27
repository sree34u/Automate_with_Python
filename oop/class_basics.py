#Python OOP
#instance variables, class variables
#class methods and static methods
#alternative constructor

class Employee:

    num_employees = 0
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@company.com'
        
        Employee.num_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
emp_1 = Employee("Sreenath", "S" , 60000 )
emp_2 = Employee("Ramesh" , "Satish", 50000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Sam-Toe-30000'
emp_str_3 = 'Damn-Doo-20000'

new_emp_1 = Employee.from_str(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)