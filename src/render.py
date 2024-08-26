import os

from state import *

def render_init():
    clear_screen()
    print('Lets play Hangman...\n')
    print('(Hit enter to continue)\n')

def render_update(state):
    clear_screen()
    show_hangman()
    print('Enter your next guess:')

def render_game_over():
    clear_screen()
    print('GAME OVER')
    print('\n\n\n\n\n')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_hangman():
    print('  ______ ')
    print(' |      |')
    print(' o      |')
    print('-|-     |')
    print('/ \\     |')
    print('       _|_')
