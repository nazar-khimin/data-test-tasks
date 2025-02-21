# class Employee:
#
#     def __init__(self, name, **kwargs):
#         self.name = name
#         self.firstname = name.split(" ")[0]
#         self.lastname = name.split(" ")[1]
#
#         for key, value in kwargs.items():
#             setattr(self, key, value)
#
#         [setattr() for key, value in kwargs.items()]
#
#
#
# giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
# print(giancarlo.name)
# print(giancarlo.nationality)


class Employee:

    def __init__(self, str_names, **kwargs):
        self.name, self.lastname = str_names.split()

        for key, value in kwargs.items():
            setattr(self, key, value)

        [setattr() for key, value in kwargs.items()]



giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
print(giancarlo.name)
print(giancarlo.nationality)