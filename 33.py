class User:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getSurname(self):
        return self.__surname
    def setSurname(self, surname):
        self.__surname = surname
    def greet(self):
        print(f"Hello, my name is {self.__name} {self.__surname}")
class Employee(User):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname)
        self.__age = age
        self.__salary = salary
    def getAge(self):
        return self.__age
    def getSalary(self):
        return self.__salary
    def display_info(self):
        print(
            f"Name: {self.getName()} {self.getSurname()}, Age: {self.__age}, Salary: {self.__salary}"
        )
employee = Employee("Михаил", "Маслов", 19, 50000)
age = employee.getAge()
salary = employee.getSalary()
print(f"Age: {age}")
print(f"Salary: {salary}")
employee.greet()
employee.display_info()
