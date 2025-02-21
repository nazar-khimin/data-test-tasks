def double_string_v1(data):
    # concatenated = {a + b for a in data for b in data}
    # count_dict = {string: sum(1 if string in concatenated else 0) for string in data}
    # count_dict = {string: sum(1 for item in concatenated if item == string) for string in data}

    # print(count_dict)
    # total_count = sum(count_dict.values())
    # return total_count
    # set comprehension -> collect all combinations
    concatenated = {a + b for a in data for b in data}
    return sum(1 for string in data if string in concatenated)

def double_string_v2(strings):
    count = 0
    strings_set = set(strings)  # Use a set for fast lookup
    print("Possible solutions:")
    for s in strings:
        for i in range(1, len(s)):
            # Split the string into two parts
            left, right = s[:i], s[i:]
            if left in strings_set and right in strings_set:
                print(f"{s} = {left} + {right}")
                count += 1
                break  # Avoid double-counting this string

    return count


def double_string_v3(strings):
    count = 0
    strings_set = set(strings)  # Use a set for fast lookup

    for s in strings:
        for i in range(1, len(s)):
            # Split the string into two parts
            left, right = s[:i], s[i:]
            if left in strings_set and right in strings_set:
                count += 1
                break  # Avoid double-counting this string

    return count


data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string_v1(data))
# print(double_string_v1(data))
# print(double_string_v2(data))
# print(double_string_v3(data))