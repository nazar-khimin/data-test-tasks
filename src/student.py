from typing import TYPE_CHECKING

from src.person import Person

if TYPE_CHECKING:
    from src.course import Course


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses: list["Course"] = []
        self.grades: dict["Course", int] = {}
        self.grade_level: int = 0

    def enroll_course(self, course: "Course"):
        self.courses.append(course)

    def add_grade(self, course: "Course", grade):
        if course not in self.courses:
            raise ValueError('Student is not enrolled in this course.')
        self.grades[course] = grade

    def calculate_gpa(self) -> float:
        """
        Note: GPA (Grade Point Average) is calculated as the sum of (grade * credits) / total credits for all courses.
        """
        total_credits = sum(course.credits for course in self.courses)
        if total_credits == 0:
            return 0
        total_grade_points = sum(grade * course.credits for course, grade in self.grades.items())
        gpa = total_grade_points / total_credits
        return round(gpa, 1)

    def __repr__(self):
        courses_names = [course.name for course in self.courses]
        return (f'Student('
                f'{super().__repr__()!r}, '
                f'courses = {courses_names!r}, '
                f'grades = {self.grades!r}, '
                f'grade_level = {self.grade_level!r}'
                f')')
