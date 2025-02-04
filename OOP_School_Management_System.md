Design and implement a School Management System using OOP principles.

Your task is to implement the following classes with their respective responsibilities:

1. Person (base class)
    - Properties: id, name
2. Student (derived from Person)
    - Properties: id, name, courses, grades, grade_level
    - Methods: enroll_course, add_grade, calculate_gpa
    - Note: GPA (Grade Point Average) is calculated as the sum of (grade * credits) / total credits for all courses.
3. Teacher (derived from Person)
    - Properties: id, name, subject_specialty, courses_teaching
    - Methods: assign_grade, add_course, remove_course
4. Course
    - Properties: id, name, teacher, students, max_capacity, required_grade_level, credits
    - Methods: add_student, remove_student, is_full, get_average_grade
5. School
    - Properties: name, students, teachers, courses
    - Methods: add_student, add_teacher, add_course, remove_student, remove_teacher, remove_course, get_student_by_id,
      get_teacher_by_id, get_course_by_id

Requirements:

1. Implement proper error handling:
    - Raise exceptions for invalid operations (e.g., enrolling in a full course, assigning grades to non-enrolled
      students, enrolling in a course without the required grade level, etc.)
    - Handle cases like student/teacher not found

2. Implement data validation:
    - Ensure unique IDs
    - Ensure grade levels are valid (1-4)
    - Ensure course credits are valid (1-5)
    - Ensure grade values are valid (0-100)

3. Use proper encapsulation:
    - Make appropriate attributes private
    - Provide getter/setter methods where necessary

4. Implement string representation:
    - All classes should have __str__ and __repr__ methods to provide a string representation of the object

5. Document your code with proper docstrings and type hints.
    - Use type hints for parameters and return types
    - Use docstrings to describe classes and methods
    - Use comments to explain complex parts of your code
    - Use descriptive variable names

6. Create a main function to demonstrate the functionality of your classes.
    - Create a school object
    - Add students, teachers, and courses
    - Enroll students in courses
    - Assign grades to students
    - Calculate GPA for students
    - Display information about students, teachers, and courses
