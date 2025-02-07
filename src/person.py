import uuid
from abc import ABC

from src.utils.repr_generator import generate_repr

@generate_repr()
class Person(ABC):

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name

    def __repr__(self):
        return f'id = {self.id!r}, name = {self.name!r}'