

class Employee:
    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

emp_1 = Employee('Jinho', 'Seo', 'pineapplebingo.dev@gmail')

print(emp_1.firstname)
print(emp_1.lastname)
print(emp_1.email)
print(emp_1.fullname())