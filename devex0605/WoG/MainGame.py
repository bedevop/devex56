# WoG, Igal

from Live import welcome, load_game, get_game_class

print(
    welcome(
        input('Player name:')
    )
)

if load_game := load_game():
    get_game_class(load_game).play()

print('GoodBye.')
