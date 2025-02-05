import uuid
from src.Student import Student
from src.utils.Errors import CourserMaxStudentsLimitException
from src.utils.Validations import validate_grade_level, validate_grade_credits


class Course:
    def __init__(self, name: str, teacher, max_capacity, required_grade_level, _credits):
        self.id = str(uuid.uuid4())
        self.name = name
        self.teacher = teacher
        self.students: list[Student] = []
        self.max_capacity = max_capacity
        self.required_grade_level = validate_grade_level(required_grade_level)
        self.credits = validate_grade_credits(_credits)

    def add_student(self, student: Student):
        if self.is_full():
            raise CourserMaxStudentsLimitException(f"Student {student.name} can't be added, courser is full.")
        self.students.append(student)
        student.enroll_course(self)

    def remove_student(self, student: Student):
        self.students.remove(student)

    def is_full(self):
        return len(self.students) == self.max_capacity

    def get_average_grade(self) -> float:
        average = sum(student.grades for student in self.students) / len(self.students)
        return round(average, 1)


def __repr__(self):
    students_name = [student.name for student in self.students]
    return (f'Course('
            f'id = {self.id!r}, '
            f'name = {self.name!r}, '
            f'teacher = {self.teacher.name!r}, '
            f'students = {students_name!r}, '
            f'max_capacity = {self.max_capacity!r}, '
            f'required_grade_level = {self.required_grade_level!r}, '
            f'credits = {self.credits!r}'
            f')')
