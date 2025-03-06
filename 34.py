class User:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
    def getName(self):
        return self.__capitalize_first(self.__name)  
    def setName(self, name):
        self.__name = name
    def getSurname(self):
        return self.__surname
    def setSurname(self, surname):
        self.__surname = surname
    def greet(self):
        print(f"Hello, my name is {self.getName()} {self.getSurname()}")  
    def __capitalize_first(self, string):  
        return string.capitalize()  
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
            f"Name: {super().getName()} {self.getSurname()}, Age: {self.__age}, Salary: {self.__salary}"
        )
    def try_use_private_method(self):
        return super().getName()  
employee = Employee("Михаил", "Маслов", 19, 50000)
print(f"Capitalized name (via getter): {employee.getName()}")
print(
    f"Name via try_use_private_method: {employee.try_use_private_method()}"
)  
employee.display_info()
