SECRET_WORD = 'CAT'
GUESSES_LEFT_KEY = 'GUESSES_LEFT'

def run_game():
    print('Lets play Hangman')
    state = init()
    while not is_game_over(state):
        state = update(state)
        render(state)

def is_game_over(state):
    return state[GUESSES_LEFT_KEY] == 0

def init():
    state = {}
    state[GUESSES_LEFT_KEY] = 3
    return state

def update(state):
    print('Enter your next guess:')
    next_guess = input()
    state[GUESSES_LEFT_KEY] -= 1
    return state

def render(state):
    print('WORD: ?')
    show_hangman()

def show_hangman():
    print('  ______ ')
    print(' |      |')
    print(' o      |')
    print('-|-     |')
    print('/ \\     |')
    print('       _|_')

run_game()
