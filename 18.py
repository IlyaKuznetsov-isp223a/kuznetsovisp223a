class Employee:
    __name = None
    __salary = None
    __age = None
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.setAge(age)
    def getName(self):
        return self.__name
    def getSalary(self):
        return f"{self.__salary}$"
    def getAge(self):
        return self.__age
    def setName(self, name):
        self.__name = name
    def setSalary(self, salary):
        self.__salary = salary
    def setAge(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            raise Exception("Age must be between 0 and 120!")
employee = Employee('Михаил', 50000, 19)
employee.setAge(35)
print(employee.getName())
print(employee.getSalary())
print(employee.getAge())
