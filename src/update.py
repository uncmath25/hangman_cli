from state import *

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
