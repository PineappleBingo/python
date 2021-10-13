

class Employee:

    num_of_emps = 0
    rais_amount = 1.04

    def __init__(self, firstname, lastname, email, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.pay = pay
        
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

emp_1 = Employee('Jinho', 'Seo', 'pineapplebingo.dev@gmail', 50000)

print(emp_1.firstname)
print(emp_1.lastname)
print(emp_1.email)
print(emp_1.fullname())

print(emp_1.__dict__)
emp_1.rais_amount = 1.05
print(emp_1.__dict__)