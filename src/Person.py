import uuid


class Person:
    def __init__(self, name):
        self.id = uuid.uuid4(),
        self.name = name

    def __repr__(self):
        return (f'id: {self.id}, '
                f'name: {self.name}')
