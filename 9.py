class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def cape(self, stri):
        return stri.capitalize()

    def initials(self):
        return self.cape(self.name)[0] + self.cape(self.surname)[0]
