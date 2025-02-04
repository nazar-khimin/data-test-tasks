import uuid


class Person:
    def __init__(self, name):
        self.id = uuid.uuid4(),
        self.name = name

    def __repr__(self):
        output = ""
        for _, var in vars(self).items():
            output += str(var)
        return output
