from src.Student import Student
from src.Teacher import Teacher
from src.Course import Course


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

    def __repr__(self):
        output = ""
        for _, var in vars(self).items():
            output += str(var)
        return output
