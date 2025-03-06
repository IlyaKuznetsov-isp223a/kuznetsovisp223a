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
    def setAge(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Age must be greater than or equal to 0")
    def getAge(self):
        return self.__age
class Employee(User):
    def __init__(self, name, surname, position, salary, age):
        super().__init__(name, surname)  
        self.__position = position
        self.__salary = salary
        self.setAge(age) 
    def getPosition(self):
        return self.__position
    def setPosition(self, position):
        self.__position = position
    def getSalary(self):
        return self.__salary
    def setSalary(self, salary):
        self.__salary = salary
    def setAge(self, age):
        if age <= 65:  
            super().setAge(age)  
        else:
            raise ValueError("Age must be less than or equal to 65 for employees")
    def display_info(self):
        print(
            f"Name: {self.getName()} {self.getSurname()}, Position: {self.__position}, Salary: {self.__salary}, Age: {self.getAge()}"
        )
employee = Employee("Михаил", "Маслоу", "Software Engineer", 100000, 19)
try:
    employee.setAge(70)  
except ValueError as e:
    print(f"Error: {e}")
employee.setAge(49)  
employee.display_info()
