# class Employee:
#     def __init__(self, firstname, lastname, salary):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.salary = salary
#
#     @staticmethod
#     def from_string(employee_string):
#         employee_map = employee_string.split("-")
#         firstname = employee_map[0]
#         lastname = employee_map[1]
#         salary = int(employee_map[2])
#         return Employee(firstname, lastname, salary)
#
#
# emp1 = Employee("Mary", "Sue", 60000)
# emp2 = Employee.from_string("John-Smith-55000")
#
# print(emp1.firstname)
# print(emp1.salary)
# print(emp2.firstname)

list

class Employee:
    def __init__(self, _firstname, _lastname, _salary):
        self.firstname = _firstname
        self.lastname = _lastname
        self.salary = _salary

    @staticmethod
    def from_string(employee_string):
        _firstname, _lastname, _salary = employee_string.split("-")
        return Employee(_firstname, _lastname, _salary)


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp1.firstname)
print(emp1.salary)
print(emp2.firstname)

