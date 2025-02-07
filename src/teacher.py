from src.person import Person

from src.course import Course
from src.student import Student
from src.utils.validations import validate_grade_value


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
        self.courses_teaching.remove(course)

    def __repr__(self):
        courses_ids = [course.id for course in self.courses_teaching]
        return (f'Teacher('
                f'{super().__repr__()}, '
                f'subject_specialty = {self.subject_specialty_list!r}, '
                f'courses_teaching = {courses_ids!r}'
                f')')
