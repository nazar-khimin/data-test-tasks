from src.person import Person

from src.course import Course
from src.student import Student
from src.utils.repr_generator import generate_repr
from src.utils.validations import validate_grade_value

@generate_repr()
class Teacher(Person):

    def __init__(self, name, subject_specialties: list[str]):
        super().__init__(name)
        self.subject_specialties: list[str] = subject_specialties
        self.courses_teaching: list[Course] = []

    def assign_grade(self, course: Course, student: Student, grade: int):
        validate_grade_value(grade)
        student.add_grade(course, grade)

    def add_course(self, course: Course):
        self.courses_teaching.append(course)
        course.teacher = self

    def remove_course(self, course: Course):
        course.teacher = None
        self.courses_teaching.remove(course)
