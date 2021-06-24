# WoG, Igal

def welcome(name):
    return 'Hello %s and welcome to the World of Games (WoG).Here you can find many cool games to play.' % name


def load_game():
    game_choices = 'Please choose a game to play:'
    games_menu = {
        1: 'Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back',
        2: 'Guess Game - guess a number and see if you chose like the computer',
        3: 'Currency Roulette - try and guess the value of a random amount of USD in ILS',
    }
    for game_number, game_desc in games_menu.items():
        game_choices += '\n\t' + str(game_number) + '. ' + game_desc
    game_choices_level = 'Please choose game difficulty from:'
    game_level_range = range(1, 6)

    load = {}
    try:
        input_game = int(input(game_choices + '\n'))
        if input_game in games_menu.keys():
            load['Game'] = input_game
            input_level = int(input(game_choices_level + str(list(game_level_range)) + '\n'))
            if input_level in game_level_range:
                load['Level'] = input_level
            else:
                raise ValueError
        else:
            raise ValueError
        return load
    except ValueError:
        return False
    finally:
        for _ in ('Game', 'Level'):
            print(_ + ':' + str(load.get(_, 'Not set or out of range')), end=' ')
        print()


def get_game_class(load):
    games_menu = {
        1: 'MemoryGame',
        2: 'GuessGame',
        3: 'CurrencyRouletteGame',
    }
    game_class = games_menu[load['Game']]
    game_level = load['Level']
    game = getattr(__import__('WoG.' + game_class,
                              fromlist=[game_class]),
                   game_class)(game_level)
    return game
