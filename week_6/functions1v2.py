#Cree dos funciones que impriman dos cosas distintas, 
# y haga que la primera llame la segunda.
level = 1

def welcome_to_game():
    print('Welcome to F1 driver')
    load_level()

def load_level():
    global level
    level += 1
    print('Loading level {level}...')

welcome_to_game()