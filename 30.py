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
    def __init__(self, name, surname, position, salary):
        super().__init__(name, surname)  
        self.__position = position
        self.__salary = salary
    def getPosition(self):
        return self.__position
    def setPosition(self, position):
        self.__position = position
    def getSalary(self):
        return self.__salary
    def setSalary(self, salary):
        self.__salary = salary
    def display_info(self):
        print(
            f"Name: {self.getName()} {self.getSurname()}, Position: {self.__position}, Salary: {self.__salary}"
        )
employee = Employee("Михаил", "Маслов", "Software Engineer", 100000)
employee.setName("Лев")
employee.setSurname("Белавин")
employee.setSalary(120000)
name = employee.getName()
surname = employee.getSurname()
salary = employee.getSalary()
print(f"Name: {name}")  
print(f"Surname: {surname}")  
print(f"Salary: {salary}")  
employee.greet()  
employee.display_info()  
