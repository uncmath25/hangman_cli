from state import *

def update(state):
    next_guess = input()
    if not is_game_started(state):
        set_game_started(state)
    else:
        add_guess(state, next_guess)
        remove_guess_left(state)
    return state
