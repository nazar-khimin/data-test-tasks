class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if not self.words:
            self.words.append(word)
        else:
            game_over = "game over"
            if word in self.words:
                self.game_over = True
                return game_over
            last_item = self.words[-1]
            if last_item[-1] != word[0]:
                self.game_over = True
                return game_over
            else:
                self.words.append(word)
        return self.words

    def restart(self):
        self.words.clear()
        self.game_over = False
        return "game restarted"


my_gallows = Gallows()
print(my_gallows.restart())
print(my_gallows.words)
print(my_gallows.game_over)
print(my_gallows.play('hostess'))
print(my_gallows.game_over, False)
print(my_gallows.play('stash'))
print(my_gallows.play('hostess'))
print(my_gallows.words)