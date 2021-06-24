# WoG, Igal

import inspect


class Game:

    def __init__(self, level):
        self.level = level

    def match(self, match):
        stack = inspect.stack()
        calling_class = stack[1][0].f_locals["self"].__class__.__name__
        prompt = calling_class + ', Level ' + str(self.level)

        print('\033[92m' if match else '\033[96m', end='')
        print(prompt + (': Good for you.' if match else ': Maybe next time.'))
        print('\033[0m', end='')
