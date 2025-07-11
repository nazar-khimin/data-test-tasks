from src.student import Student
from src.teacher import Teacher
from src.course import Course
from src.utils.repr_generator import generate_repr


@generate_repr(fields={"students": "name", "teachers": "name"})
class School:

    def __init__(self, name: str):
        self.name = name
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []
        self.courses: list[Course] = []

    def add_student(self, student: Student):
        self.students.append(student)

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def add_course(self, course: Course):
        self.courses.append(course)

    def remove_student(self, student: Student):
        self.students.remove(student)

    def remove_teacher(self, teacher: Teacher):
        self.teachers.remove(teacher)

    def remove_course(self, course: Course):
        self.courses.remove(course)
