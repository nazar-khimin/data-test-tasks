from src.Person import Person

from src.Course import Course


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.subject_specialty: str = ''
        self.courses_teaching: list[Course] = []

    def assign_grade(self):
        pass

    def add_course(self, course: Course):
        self.courses_teaching.append(course)
        pass

    def remove_course(self):
        pass

    def __repr__(self):
        return (f' subject_specialty = {self.subject_specialty}, '
                f'courses_teaching = {self.courses_teaching}')
