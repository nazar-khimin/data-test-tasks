from enum import Enum
import json
from typing import List
import uuid


class NonUniqueException(Exception):
    pass


class PasswordValidationException(Exception):
    pass


class ForbiddenException(Exception):
    pass


class Role(Enum):
    Mentor = 1
    Trainee = 0


class Score(Enum):
    D = "D"
    B = "B"
    C = "C"
    A = "A"


class Subject:

    def __init__(self, title: str, id: str = None):
        self.title = title
        if id:
            self.id = id
        else:
            self.id = str(uuid.uuid4())

    def __repr__(self):
        return f'{self.title}'


class Grade:
    def __init__(self, subject: Subject, score: Score):
        self.subject = subject
        self.score = score

    def __repr__(self):
        return f"{{'{self.subject.title}': '{self.score.value}'}}"


class User:
    def __init__(self, username: str, _id: uuid, role: Role, password: str):
        self.username = username
        self.id: uuid = _id
        self.role = role
        self.password = password
        self.grades = []

    @classmethod
    def create_user(cls, username: str, password: str, role: Role):
        user_id = uuid.uuid4()
        if password == 'InvalidPassword':
            raise PasswordValidationException()
        return cls(username, user_id, role, password)

    def add_grade(self, grade: Grade):
        self.grades.append(grade)

    def add_score_for_subject(self, subject: Subject, score: Score):
        existing_grade = next((g for g in self.grades if g.subject.id == subject.id), None)
        if existing_grade:
            existing_grade.score = score
        else:
            self.grades.append(Grade(subject, score))

    def __repr__(self):
        return f"{self.username} with role {self.role.__class__.__name__}.{self.role.name}: {self.grades}"


def get_subjects_from_json(subjects_json: str) -> List[Subject]:
    with open(subjects_json, 'r') as f:
        subjects = json.load(f)
    return [Subject(subject['title'], subject['id']) for subject in subjects]


def get_users_with_grades(users_json: str, subjects_json: str, grades_json: str) -> List[User]:
    with open(users_json, 'r') as f:
        users = json.load(f)
    with open(subjects_json, 'r') as f:
        subjects = json.load(f)
    with open(grades_json, 'r') as f:
        grades = json.load(f)
    users_with_grades = []
    subjects_list = [Subject(subject['title'], subject['id']) for subject in subjects]
    for user in users:
        user_obj = User(user['username'], user['id'], Role(user['role']), user['password'])
        for grade in grades:
            if grade['user_id'] == user['id']:
                subject = next((subject for subject in subjects_list if subject.id == grade['subject_id']), None)
                if subject:
                    score = Score(grade['score'])
                    user_obj.add_grade(Grade(subject, score))
        users_with_grades.append(user_obj)
    return users_with_grades


def add_user(user: User, users: List[User]):
    for u in users:
        if u.username == user.username:
            raise NonUniqueException(f"User with name {u.username} already exists")
    users.append(user)


def add_subject(subject: Subject, subjects: List[Subject]):
    for s in subjects:
        if s.id == subject.id:
            return
    subjects.append(subject)


def check_if_user_present(username, password, users: List[User]):
    for u in users:
        if username == u.username and password == u.password:
            return True
    return False


def get_grades_for_user(username: str, user, users: List[User]) -> List[Grade]:
    if username != user.username and user.role != Role.Mentor:
        raise ForbiddenException("Forbidden")

    for user in users:
        if user.username == username:
            return user.grades
    return []


def users_to_json(users: List[User], json_file: str):
    users_data = []
    for user in users:
        users_data.append({
            "username": user.username,
            "id": str(user.id),
            "role": user.role.value,
            "password": user.password
        })
    with open(json_file, 'w') as f:
        json.dump(users_data, f)


def subjects_to_json(subjects: List[Subject], json_file: str):
    subjects_data = []
    for subject in subjects:
        subjects_data.append({
            "title": subject.title,
            "id": subject.id
        })
    with open(json_file, 'w') as f:
        json.dump(subjects_data, f)


def grades_to_json(users: List[User], subjects: List[Subject], json_file: str):
    grades_data = []
    for user in users:
        for grade in user.grades:
            grades_data.append({
                "user_id": str(user.id),
                "subject_id": grade.subject.id,
                "score": grade.score.value
            })
    with open(json_file, 'w') as f:
        json.dump(grades_data, f)


users = get_users_with_grades("users.json", "subjects.json", "grades.json")
print(len(users))

subjects = get_subjects_from_json("subjects.json")
print(len(subjects))

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(mentor)

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
student = User.create_user("Mentor", "!1qQ456", Role.Trainee)
try:
    add_user(student, users)
except NonUniqueException as e:
    print(str(e))

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(check_if_user_present("Mentor", "aaaaaa", users))
print(check_if_user_present("Mentor", "!1qQ456", users))

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
print(get_grades_for_user("Trainee1", users[1], users))

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
print(len(users))
print(user2)

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

print(get_grades_for_user("Trainee1", users[1], users))

try:
    user = User.create_user("Name", "InvalidPassword", Role.Trainee)
except PasswordValidationException:
    print("Invalid password")

user = User.create_user("Name", "6_Vow&", Role.Trainee)
print(type(user.id).__name__)

users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 = User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

try:
    print(get_grades_for_user("Second", users[0], users))
except ForbiddenException:
    print("Forbidden")
print(get_grades_for_user("Second", users[2], users))



users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

users_to_json(users, "345.json")



users = get_users_with_grades("users.json", "subjects.json", "grades.json")
subjects = get_subjects_from_json("subjects.json")
mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
add_user(mentor, users)
user2 =  User.create_user("Second", "Password_0", Role.Trainee)
add_user(user2, users)
user2.add_score_for_subject(subjects[1], Score.B)
subject = Subject("New Subject")
add_subject(subject, subjects)
users[0].add_score_for_subject(subject, Score.D)

grades_to_json(users, subjects, "987.json")

def main():
    subjects_json = 'subjects.json'
    users_json = 'users.json'
    grades_json = 'grades.json'

    subjects = get_subjects_from_json(subjects_json)
    users = get_users_with_grades(users_json, subjects_json, grades_json)

    mentor = User.create_user("Mentor", "!1qQ456", Role.Mentor)
    subject1 = next((subject for subject in subjects if subject.title == 'Mathematics'), None)
    if subject1:
        mentor.add_score_for_subject(subject1, 'A')
    subject2 = next((subject for subject in subjects if subject.title == 'Software Design'), None)
    if subject2:
        mentor.add_score_for_subject(subject2, 'B')

    add_user(mentor, users)

    users_to_json(users, 'new_users.json')
    subjects_to_json(subjects, 'new_subjects.json')
    grades_to_json(users, subjects, 'new_grades.json')

if __name__ == "__main__":
    main()
