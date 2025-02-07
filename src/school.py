from src.student import Student
from src.teacher import Teacher
from src.course import Course


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
        courses_name = [course.name for course in self.courses]
        teachers_name = [teacher.name for teacher in self.teachers]
        students_name = [student.name for student in self.students]
        return (f'School('
                f'name = {self.name!r}, '
                f'students = {students_name!r}, '
                f'teachers = {teachers_name!r}, '
                f'courses = {courses_name!r}'
                f')')
