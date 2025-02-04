import uuid
from src.Student import Student


class Course:
    def __init__(self, name: str, teacher, max_capacity, required_grade_level, _credits):
        self.id = uuid.uuid4()
        self.name = name
        self.teacher = teacher
        self.students: list[Student] = []
        self.max_capacity = max_capacity
        self.required_grade_level = required_grade_level
        self.credits = _credits

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, student: Student):
        self.students.remove(student)

    def is_full(self):
        pass

    def get_average_grade(self):
        pass

    def __repr__(self):
        return (f'id = {self.id}, name = {self.name}, teacher = {self.teacher}, '
                f'students = {self.students}, max_capacity = {self.max_capacity}, '
                f'max_capacity = {self.max_capacity}, required_grade_level = {self.required_grade_level}, '
                f'credits = {self.credits}')
