class Student:
    name = "михаил"
    surname = "маслов"
    def show(self):
        return f"{self.cape()} {self.initials()}"
    def cape(self):
        return f"{self.name.title()} {self.surname.title()}"
    def initials(self):
        return f"{self.name[0]}.{self.surname[0]}"
student = Student()
print(student.show())
