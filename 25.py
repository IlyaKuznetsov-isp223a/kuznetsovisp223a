class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
class EmployeesCollection:
    def __init__(self):
        self.__employees = [] 
    def add(self, employee):
        self.__employees.append(employee)
    def show(self):
        for employee in self.__employees:
            print(f"Имя: {employee.getName()}, Зарплата: {employee.getSalary()}")
    def getTotalSalary(self):
        total_salary = 0
        for employee in self.__employees:
            total_salary += employee.getSalary()
        return total_salary
    def getAverageSalary(self):
        if not self.__employees:  
            return 0
        return self.getTotalSalary() / len(self.__employees)
employees_collection = EmployeesCollection()
employees_collection.add(Employee("Михаил", 50000))
employees_collection.add(Employee("Лев", 60000))
employees_collection.add(Employee("Никита", 70000))
print("Все работники:")
employees_collection.show()
total_salary = employees_collection.getTotalSalary()
print(f"\nСуммарная зарплата: {total_salary}")
average_salary = employees_collection.getAverageSalary()
print(f"Средняя зарплата: {average_salary}")
