GUESSES_LEFT_KEY = 'GUESSES_LEFT'
GUESSES_KEY = 'GUESSES'
IS_GAME_STARTED_KEY = 'IS_GAME_STARTED'
HAS_ASKED_GAME_TO_START_KEY = 'HAS_ASKED_GAME_TO_START'

def init(init_guesses):
    state = {}
    state[GUESSES_LEFT_KEY] = init_guesses
    state[GUESSES_KEY] = []
    state[IS_GAME_STARTED_KEY] = False
    state[HAS_ASKED_GAME_TO_START_KEY] = False
    return state

def is_game_started(state):
    return state[IS_GAME_STARTED_KEY]

def set_game_started(state):
    state[IS_GAME_STARTED_KEY] = True

def has_asked_game_to_start(state):
    return state[HAS_ASKED_GAME_TO_START_KEY]

def ask_game_to_start(state):
    state[HAS_ASKED_GAME_TO_START_KEY] = True

def is_game_over(state):
    return state[GUESSES_LEFT_KEY] == 0

def add_guess(state, guess):
    state[GUESSES_KEY].append(guess)

def remove_guess_left(state):
    state[GUESSES_LEFT_KEY] -= 1
