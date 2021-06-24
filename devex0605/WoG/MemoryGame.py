# WoG, Igal

import random
import time
from colored import fg, attr
from WoG.Game import Game


class MemoryGame(Game):

    def __init__(self, level):
        super().__init__(level)
        self.sequence = []

    def play(self):
        self.generate_sequence()
        list_from_user = self.get_list_from_user()
        self.is_list_equal(self.sequence, list_from_user)

    def generate_sequence(self):
        for _ in range(1, self.level + 1):
            self.sequence.append(random.randint(1, 101))
        print(fg(127) + attr(1) + (str(self.sequence)).strip('[]'), end='')
        time.sleep(0.7)
        print(attr('reset'), end='\r')

    def get_list_from_user(self):
        prompt = 'Input the {}-sized list by recall :'.format(self.level)
        list_input = []
        try:
            list_input = [int(_) for _ in input(prompt).split(',')]
        except ValueError:
            print('Expected a list of integers')
        finally:
            return list_input

    def is_list_equal(self, sequence, list_from_user):
        self.match(sequence == list_from_user)
