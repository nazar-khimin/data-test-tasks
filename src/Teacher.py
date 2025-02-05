from src.Person import Person

from src.Course import Course
from src.Student import Student
from src.utils.Validations import validate_grade_value


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.subject_specialty: str = ''
        self.courses_teaching: list[Course] = []

    def assign_grade(self, course: Course, student: Student, grade: int):
        validate_grade_value(grade)
        student.add_grade(course, grade)

    def add_course(self, course: Course):
        self.courses_teaching.append(course)
        course.teacher = self

    def remove_course(self, course: Course):
        self.courses_teaching.remove(course)

    def __repr__(self):
        courses_ids = [course.id for course in self.courses_teaching]
        return (f'Teacher('
                f'{super().__repr__()}, '
                f'subject_specialty = {self.subject_specialty!r}, '
                f'courses_teaching = {courses_ids!r}'
                f')')
