# WoG, Igal

import random
from WoG.Game import Game


class GuessGame(Game):

    def __init__(self, level):
        super().__init__(level)
        self.secret_number = None

    def play(self):
        self.generate_number()
        guess = self.get_guess_from_user()
        self.compare_results(guess)

    def generate_number(self):
        self.secret_number = random.randint(1, self.level)

    def get_guess_from_user(self):
        prompt = 'A number between 1 to ' + str(self.level)
        try:
            input_guess = int(input(prompt + ':'))
            if input_guess in range(1, self.level + 1):
                return input_guess
            else:
                raise ValueError
        except ValueError:
            return 0

    def compare_results(self, guess):
        self.match(guess == self.secret_number)
