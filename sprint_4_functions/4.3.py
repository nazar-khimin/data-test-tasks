import re


def create_account(user_name: str, password: str, secret_words: list):
    pattern = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^A-Za-z0-9]).{6,}$"

    if not re.match(pattern, password):
        raise ValueError("Password does not meet the required criteria.")

    def check(input_password: str, input_secret_words: list):
        if input_password != password:
            return False

        if len(input_secret_words) != len(secret_words):
            return False

        misspelled_count = sum(1 for word in input_secret_words if word not in secret_words)

        if misspelled_count > 1:
            return False

        return True

    return check


tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_", ["1", "word"])
check2 = tom("Qwerty1_", ["word"])
check3 = tom("Qwerty1_", ["word", "2"])
check4 = tom("Qwerty1!", ["word", "12"])

tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_", ["1", "word"])
check2 = tom("Qwerty1_", ["word"])
check3 = tom("Qwerty1_", ["word", "2"])
check4 = tom("Qwerty1!", ["word", "12"])