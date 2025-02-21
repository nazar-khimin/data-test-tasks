import os
import json
from json import JSONEncoder


class StudentEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return {
                "full_name": f"{obj.name} from {obj.group}",
                "avg_rank": obj.avg,
                "courses": obj.courses
            }
        if isinstance(obj, Group):
            return {
                "title": obj.title,
                "students": [
                    {"full_name": f"{s.name} from {s.group}",
                     "avg_rank": s.avg,
                     "courses": s.courses} for s in obj.students
                ]
            }
        return super().default(obj)


class Student:
    def __init__(self, name=None, group=None, avg=None, courses=None, full_name=None, avg_rank=None, **kwargs):
        if full_name:
            self.name, self.group = full_name.split(" from ")
        else:
            self.name = name
            self.group = group
        self.avg = avg_rank if avg_rank is not None else avg
        self.courses = courses

    def __repr__(self) -> str:
        return f"{self.name} from {self.group} ({self.avg}): {self.courses}"

    @classmethod
    def from_json(cls, json_file: str) -> 'Student':
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"{json_file} does not exist.")

        with open(json_file, 'r') as f:
            data = json.load(f)
            full_name = data["full_name"]
            name, group = full_name.split(" from ")
            return cls(
                name=name,
                group=group,
                avg=data["avg_rank"],
                courses=data["courses"]
            )

    def serialize_to_json(self, filename: str) -> None:
        with open(filename, 'w') as f:
            json.dump({
                "full_name": f"{self.name} from {self.group}",
                "avg_rank": self.avg,
                "courses": self.courses
            }, f, separators=(', ', ': '))


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    def __repr__(self) -> str:
        student_reprs = [str(student) for student in self.students]
        return f"{self.title}: {student_reprs}"

    @staticmethod
    def serialize_to_json(groups: list, filename: str) -> None:
        with open(filename, 'w') as f:
            json.dump([
                {
                    "title": g.title,
                    "students": [
                        {"full_name": f"{s.name} from {s.group}",
                         "avg_rank": s.avg,
                         "courses": s.courses} for s in g.students
                    ]
                } for g in groups
            ], f, separators=(', ', ': '))

    @classmethod
    def create_group_from_file(cls, students_file: str) -> 'Group':
        if not os.path.exists(students_file):
            raise FileNotFoundError(f"{students_file} does not exist.")

        with open(students_file, 'r') as f:
            data = json.load(f)

        students = []
        if isinstance(data, dict):  # Single student data format
            student = Student(
                name=data["full_name"].split(" from ")[0],
                group=data["full_name"].split(" from ")[1],
                avg=data["avg_rank"],
                courses=data["courses"]
            )
            students = [student]
        elif isinstance(data, list):  # Multiple students data format
            for student_data in data:
                student = Student(
                    name=student_data["full_name"].split(" from ")[0],
                    group=student_data["full_name"].split(" from ")[1],
                    avg=student_data["avg_rank"],
                    courses=student_data["courses"]
                )
                students.append(student)
        else:
            raise ValueError(f"Invalid data format in file: {students_file}")

        title = os.path.splitext(os.path.basename(students_file))[0]
        return cls(title=title, students=students)