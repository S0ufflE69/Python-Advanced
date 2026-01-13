class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return "I am " + self.name


class Student(Person):
    def info(self):
        return "I am student " + self.name


p = Person("Daniya")
s = Student("Arai")

print(p.info())
print(s.info())
