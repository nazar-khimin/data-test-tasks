from collections import OrderedDict

def sort_students_by_name(students):
    # Sort the dictionary by keys (student names) and return an OrderedDict
    sorted_students = sorted(students.items(), key= lambda item: item[1], reverse=True)  # sorts by the keys (names) by default
    return dict(sorted_students)

students = {"John": 85, "Alice": 90, "Bob": 78}
result = sort_students_by_name(students)
print(result)

students = {"Zara": 92, "Mike": 87, "Anna": 75}
result = sort_students_by_name(students)
print(result)

students = {"Olga": 88}
result = sort_students_by_name(students)
print(result)

students = {}
result = sort_students_by_name(students)
print(result)

students = {"Daniel": 65, "Chris": 85, "Bob": 72, "Alice": 95}
result = sort_students_by_name(students)
print(result)