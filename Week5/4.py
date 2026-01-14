class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def __init__(self, salary, bonus=1000):
        super().__init__(salary)  
        self._bonus = bonus      

    def get_salary(self):
        return self._salary + self._bonus 
    def get_role(self):
        return "Manager"


e1 = Employee(3000)
m1 = Manager(3000)

print(e1.get_salary())  
print(m1.get_salary())  
