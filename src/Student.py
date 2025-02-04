from typing import TYPE_CHECKING
from src.Person import Person
from src.utils.Validations import validate_grade_value

if TYPE_CHECKING:
    from src.Course import Course


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses: list["Course"] = []
        self.grades: list[int] = []
        self.grade_level: list[int] = []

    def enroll_course(self, course: "Course"):
        self.courses.append(course)

    def add_grade(self, grade):
        validate_grade_value(grade)
        pass

    def calculate_gpa(self):
        """
        Note: GPA (Grade Point Average) is calculated as the sum of (grade * credits) / total credits for all courses.
        """
        pass

    def __repr__(self):
        return (f' courses = {self.courses}, '
                f'grades = {self.grades}, '
                f'grade_level = {self.grade_level}')
