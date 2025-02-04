@staticmethod
def validate_grade_level(grade: int):
    if not 1 < grade < 4:
        raise ValueError("Grade must be between 1 and 4")
    return grade
