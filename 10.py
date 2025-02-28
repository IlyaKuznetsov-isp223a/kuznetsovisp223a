class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
employee = Employee('Михаил', 'Маслов')
print(employee.name, employee.surname)
