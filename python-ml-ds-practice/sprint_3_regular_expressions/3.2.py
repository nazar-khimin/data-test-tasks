def convert_digit_to_morse(digit):
    """Convert a single digit to Morse code."""
    # Morse code map for digits 0-9
    morse_code_map = {
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'
    }

    return morse_code_map[digit]


def morse_number(number):
    result = ""
    for digit in number:
        result += convert_digit_to_morse(digit) + " "  # Adding a space between digits
    return result.strip()  # Stripping the trailing space


# Test case
# print(morse_number("784"))  # Expected: --... ---.. ....-

# Test case
# print(morse_number("784"))  # Expected: --... ---.. ....-

# Example usage:
print(morse_number("295"))  # Expected output: ..--- ----. .....
print(morse_number("005"))  # Expected output: ----- ----- .....
print(morse_number("513"))  # Expected output: ..... .---- ...--
print(morse_number("784"))  # Expected output: --... ---.. ....-
