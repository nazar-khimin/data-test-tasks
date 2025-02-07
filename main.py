from src.school import School
from src.student import Student
from src.teacher import Teacher
from src.course import Course

# prepare data
school = School("СЗШ 32")
student1 = Student("Nazar")
student2 = Student("Bohdan")
teacher1 = Teacher("Mykola", ["Math", "Biology"])
course1 = Course("Math", teacher1, 5, 4, 4)
course2 = Course("Biology", teacher1, 5, 3, 4)

# add teacher and student to course
teacher1.add_course(course1)
course1.add_student(student1)
course1.add_student(student2)
teacher1.add_course(course2)
course2.add_student(student1)
course2.add_student(student2)

# assign grade
teacher1.assign_grade(course1, student1, 70)
teacher1.assign_grade(course1, student2, 70)
teacher1.assign_grade(course2, student1, 80)
teacher1.assign_grade(course2, student2, 80)

# add all to school
school.add_student(student1)
school.add_student(student2)
school.add_teacher(teacher1)
school.add_course(course1)
school.add_course(course2)

# calculate GPA for students
gpa1 = student1.calculate_gpa()
gpa2 = student2.calculate_gpa()
print(f'GPA for student {student1.name} : {gpa1}')
print(f'GPA for student {student2.name} : {gpa2}')

# display information about students, teacher, and courses
print(course1)
print(course2)
