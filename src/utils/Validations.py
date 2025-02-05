def validate_grade_level(grade: int):
    if not 1 <= grade <= 4:
        raise ValueError("Grade level must be between 1 and 4")
    return grade


def validate_grade_value(grade: int):
    if not 0 <= grade <= 100:
        raise ValueError("Grade value must be between 0 and 100")
    return grade


def validate_grade_credits(grade: int):
    if not 0 <= grade <= 5:
        raise ValueError("Grade value must be between 1 and 5")
    return grade
