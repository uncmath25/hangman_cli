import os

from state import *

def render(state):
    clear_screen()
    if not is_game_started(state):
        print('Lets play Hangman...\n')
    if is_game_over(state):
        print('GAME OVER')
        print('\n\n\n\n\n')
        return
    show_hangman()
    print('Enter your next guess:')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_hangman():
    print('  ______ ')
    print(' |      |')
    print(' o      |')
    print('-|-     |')
    print('/ \\     |')
    print('       _|_')
