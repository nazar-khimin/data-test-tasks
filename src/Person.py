import uuid


class Person:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name

    def __repr__(self):
        return f'id = {self.id!r}, name = {self.name!r}'
