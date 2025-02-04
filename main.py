from src.School import School
from src.Student import Student
from src.Teacher import Teacher
from src.Course import Course

# prepare data
school = School("СЗШ 32")
student1 = Student("Nazar")
teacher1 = Teacher("Mykola")
course = Course("Math", teacher1, 5, 4, 5)

# add teacher and student to course
teacher1.add_course(course)
course.add_student(student1)

# assign grade
# teacher1.assign_grade(course, teacher1)

# add all to school
school.add_student(student1)
school.add_teacher(teacher1)
school.add_course(course)

# calculate GPA for students
gpa = student1.calculate_gpa()
print(f'GPA for student {student1.name} : {gpa}')

# display information about students, teacher, and courses
print(course)
