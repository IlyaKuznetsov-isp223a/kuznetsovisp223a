class User:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print(f"Hello, my name is {self.name}")
class Employee(User):
  def __init__(self, name, position, salary):
    super().__init__(name) 
    self.position = position
    self.salary = salary
  def display_info(self):
    print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")
user = User("Михаил")
user.greet()
employee = Employee("Лев", "Software Engineer", 100000)
employee.greet()  
employee.display_info()
