import uuid
from src.Student import Student
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
        self.students.append(student)
        student.enroll_course(self)

    def remove_student(self, student: Student):
        self.students.remove(student)

    def is_full(self):
        pass

    def get_average_grade(self):
        pass

    def __repr__(self):
        return (f"Course(id = {self.id}, name = {self.name},"
                f'teacher = {self.teacher},'
                f'students = {self.students},'
                f'max_capacity = {self.max_capacity},'
                f'required_grade_level = {self.required_grade_level},'
                f'credits = {self.credits}'
                f')')
