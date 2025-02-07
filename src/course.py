import uuid
from src.student import Student
from src.utils.errors import CourseMaxStudentsLimitException
from src.utils.repr_generator import generate_repr
from src.utils.validations import validate_grade_level, validate_grade_credits


@generate_repr(fields={"students": "name", "teacher": "name"})
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
            raise CourseMaxStudentsLimitException(f"Student {student.name} can't be added, courser is full.")
        self.students.append(student)
        student.enroll_course(self)

    def remove_student(self, student: Student):
        self.students.remove(student)

    def is_full(self):
        return len(self.students) == self.max_capacity

    def get_average_grade(self) -> float:
        average = sum(student.grades for student in self.students) / len(self.students)
        return round(average, 1)
