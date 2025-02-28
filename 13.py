class Employee:
    __name = None
    __salary = None
    __age = None
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def show_info(self):
        return f'Имя: {self.__name}, Зарплата: {self.__salary}, Возраст: {self.__age}'
employee = Employee('Михаил', 50000, 19)
print(employee.show_info())
