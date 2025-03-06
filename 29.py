class User:
    def __init__(self, name):
        self.name = name
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print(f"Hello, my name is {self.name}")
class Employee(User):
    def __init__(self, name, position, salary):
        super().__init__(name)  
        self.position = position
        self.salary = salary
    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")
employee = Employee("Михаил", "Software Engineer", 100000)
employee.setName("Михаил Маслов")
name = employee.getName()
print(f"Employee name: {name}")
employee.greet()
employee.display_info()
