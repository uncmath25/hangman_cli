import os

from state import *

SECRET_WORD = 'CAT'
INITIAL_GUESSES = 3

def run_game():
    state = init(INITIAL_GUESSES)
    while not is_game_over(state):
        state = update(state)
        render(state)

def update(state):
    if not is_game_started(state):
        if not has_asked_game_to_start(state):
            ask_game_to_start(state)
            return state
        else:
            set_game_started(state)
    next_guess = input()
    add_guess(state, next_guess)
    remove_guess_left(state)
    return state

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

run_game()
