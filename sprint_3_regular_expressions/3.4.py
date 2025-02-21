import re

def pretty_message(data):
    # This function removes duplicated sequences at the end of words
    def remove_repeats(word):
        # Try to detect repeated characters or patterns at the end of the word
        for i in range(1, len(word)):
            if word[:i] == word[i:i+i]:  # If the first i characters repeat after the i-th character
                return word[:i]  # Return the base part of the word
        return word  # If no repetition, return the word as is

    # Regular expression to find words in the string
    result = re.sub(r'\b\w+\b', lambda match: remove_repeats(match.group(0)), data)

    return result

# Test case
data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data))  # Expected output: "This is echo string. Replace repeated groups of symbols"