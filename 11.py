class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
employee = Employee('Михаил', 50000)
print(employee.name, employee.salary)
