def validate_grade_level(grade_level: int):
    if not 1 <= grade_level <= 4:
        raise ValueError("Grade level must be between 1 and 4")
    return grade_level


def validate_grade_value(grade_value: int):
    if not 0 <= grade_value <= 100:
        raise ValueError("Grade value must be between 0 and 100")
    return grade_value


def validate_grade_credits(grade_credits: int):
    if not 0 <= grade_credits <= 5:
        raise ValueError("Grade value must be between 1 and 5")
    return grade_credits
