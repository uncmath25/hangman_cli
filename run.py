def run_game():
    print('Lets play Hangman')
    guesses_left = 3
    while guesses_left > 0:
        print('Enter your next guess:')
        next_guess = input()
        show_screen()
        guesses_left = guesses_left - 1
    print('GAME OVER!!!')

def show_screen():
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
