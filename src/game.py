from render import render_init, render_update, render_game_over
from state import init, is_game_over
from update import update

def run_game(word, guesses):
    state = init(word, guesses)
    render_init()
    while not is_game_over(state):
        state = update(state)
        render_update(state)
    render_game_over()
