class Employee:
    def __init__(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return 1000


def show_all(workers):
    for w in workers:
        print(w.get_role(), "-", w.get_salary())


e1 = Employee(3000)
e2 = Manager(5000)

show_all([e1, e2])
