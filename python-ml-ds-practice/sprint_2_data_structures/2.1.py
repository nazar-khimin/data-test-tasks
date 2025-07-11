from collections import namedtuple

Student = namedtuple('student', ['name', 'age', 'grade'])


def analyze_students(students):
    if not students:
        return {'average_grade': None, 'top_students': []}

    # Calculate the average grade
    total_grade = sum(student.grade for student in students)
    average_grade = round(total_grade / len(students), 1)

    # Find the highest grade
    highest_grade = max(student.grade for student in students)

    # Find students with the highest grade
    top_students = [student for student in students if student.grade == highest_grade]

    return {
        'average_grade': average_grade,
        'top_students': top_students
    }


# Example usage:

students = [
    Student(name="Олег", age=20, grade=85),
    Student(name="Анна", age=22, grade=92),
    Student(name="Марія", age=21, grade=78),
    Student(name="Іван", age=23, grade=92)
]

result = analyze_students(students)
print("Result 1: ",
      result)  # {'average_grade': 86.8, 'top_students': [Student(name='Анна', age=22, grade=92), Student(name='Іван', age=23, grade=92)]}

students = [
    Student(name="Олег", age=20, grade=100),
    Student(name="Анна", age=22, grade=100),
    Student(name="Марія", age=21, grade=95)
]

result = analyze_students(students)
print("Result 2: ",
      result)  # {'average_grade': 98.3, 'top_students': [Student(name='Олег', age=20, grade=100), Student(name='Анна', age=22, grade=100)]}

students = [
    Student(name="Олег", age=20, grade=50),
    Student(name="Анна", age=22, grade=65),
    Student(name="Марія", age=21, grade=75)
]

result = analyze_students(students)
print("Result 3: ", result)  # {'average_grade': 63.3, 'top_students': [Student(name='Марія', age=21, grade=75)]}

students = []
result = analyze_students(students)
print("Result 4: ", result)  # {'average_grade': None, 'top_students': []}
