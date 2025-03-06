class Employee:
  def __init__(self, name, salary):
    self.__name = name  
    self.__salary = salary 
  def getName(self):
    return self.__name
  def getSalary(self):
    return self.__salary
employees = [
    Employee("Михаил", 50000),
    Employee("Лев", 60000),
    Employee("Никита", 70000),
]
for employee in employees:
  print(f"Имя: {employee.getName()}, Зарплата: {employee.getSalary()}")
