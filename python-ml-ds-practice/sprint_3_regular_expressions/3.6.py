import re


def pretty_message(data):
    # Regular expression to match the title, author, and year
    pattern = r'"([^:]+(?:\s*:\s*[^"]*)*):\s([^,]+),\s(\d{4})"'

    # Find all matches using the regular expression
    matches = re.findall(pattern, data)

    # Return each match as a tuple (title, author, year)
    return matches


# Input string
data = '"Design Patterns in Java: Gang of Four, 1994", "Introduction to Algorithms: Thomas H. Cormen, 2009" - "Clean Code: Robert C. Martin, 2008"; "The Pragmatic Programmer: Andrew Hunt, 1999" and "Artificial Intelligence: A Modern Approach: Stuart Russell, 2003"'

# Loop through the results and print them
for item in pretty_message(data):
    print(item)
