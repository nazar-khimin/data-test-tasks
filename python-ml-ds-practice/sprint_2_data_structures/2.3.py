from collections import Counter


def count_characters(text):
    if not text:
        return {}

    result: dict[str, int] = {}
    text_characters = list(text)

    for c in text_characters:
        result[c] = result.get(c, 0) + 1

    # Use Counter to count the frequency of each character in the string
    # return dict(Counter(text))
    return result


def test_count_characters():
    test_cases = {
        "hello world": {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1},
        "test": {'t': 2, 'e': 1, 's': 1},
        "": {},
        "aabbcc": {'a': 2, 'b': 2, 'c': 2},
        "Python Programming": {'P': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2,
                               'i': 1}
    }
    for k, v in test_cases.items():
        result = count_characters(k)
        assert result == v, f'Expected: {v}, actual:{result}'
    print("All tests passed")


test_count_characters()
