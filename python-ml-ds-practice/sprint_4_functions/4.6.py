import random


def randomWord(word_list):
    if not word_list:
        yield None
        return

    # Initially, shuffle the list to start
    while True:
        random.shuffle(word_list)  # Shuffle the list before each cycle
        for word in word_list:
            yield word