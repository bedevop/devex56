# WoG, Igal

import random
import requests
from bs4 import BeautifulSoup
from WoG.Game import Game


class CurrencyRouletteGame(Game):

    def __init__(self, level):
        super().__init__(level)
        self.random_amount = None
        self.interval = None
        self.input_guess = 0

    def play(self):
        self.get_money_interval()
        self.get_guess_from_user()
        min_int, max_int = self.interval
        self.match(min_int <= self.input_guess <= max_int)

    def get_money_interval(self):
        url = "https://www.investing.com/currencies/usd-ils-advanced-chart"
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
                                 "Chrome/22.0.1207.1 Safari/537.1"}
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.text, 'html.parser')
        rate = soup.find(id='last_last').text

        self.random_amount = random.randint(2, 100)
        total_value = self.random_amount * float(rate)
        offset = 5 - self.level
        self.interval = (total_value - offset, total_value + offset)

    def get_guess_from_user(self):
        prompt = 'Guess what is the value of {} ILS in USD :'.format(self.random_amount)
        try:
            self.input_guess = float(input(prompt))
        except ValueError:
            print('Expected integer or float')
