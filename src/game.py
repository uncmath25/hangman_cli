from render import render
from state import init, is_game_over
from update import update

def run_game(word, guesses):
    state = init(word, guesses)
    while not is_game_over(state):
        state = update(state)
        render(state)
