from random import randint
from os import system
import platform

#------------------------------------------------------------------------
def clearScreen():
    operating_system = platform.system()
    if operating_system == 'Windows':
        system('cls')
    elif operating_system == 'Darwin' or operating_system == 'Linux':
        system('clear')
#------------------------------------------------------------------------
def isPlaying():
    flag = True
    while flag:
        is_playing = input('(y/n): ')
        if is_playing == 'y' or is_playing == 'n':
            flag = False
        
    if is_playing == 'y':
        game()
    else:
        end_screen()

def game():
    clearScreen()
    word = getRandomWord()
    guess_squares = []
    ending = f'You Lose! The word was {word}'
    number_of_guesses = 6
    letters = []

    while number_of_guesses != 0:
        guess = input('Guess: ').lower()
        if guessCheck(guess):
            if guess == word:
                ending = 'You Win!'
                break
            else:
                squares = (guessInWord(guess, word))
                prev_guess = (guess)
                prev_guess_squares = f'{prev_guess} {squares}'
                guess_squares.append(prev_guess_squares)
            number_of_guesses -= 1
        else:
            guess = ''
            print('INVALID WORD')
            cont = input('Press "Enter" to continue.')

        clearScreen()
        for x in get_letters(guess, word):
            if x not in letters:
                letters.append(x)
        print('Letters in random word: ' + ' '.join(str(y) for y in letters))
        print('\n'.join(guess_squares))
    
    print(ending)
    print("Would you like to play again?")
    isPlaying()

def getRandomWord():
    with open('words.txt') as f:
        words = f.read().splitlines()
    rand_int = randint(0, len(words) - 1)

    return words[rand_int]

def guessCheck(guess):
    with open('all-words.txt') as f:
        words = f.read().splitlines()

    if guess in words:
        return True

def guessInWord(guess, word):
    
    green_square = '\U0001f7e9' #Correct Letter/Place
    red_square = '\U0001f7e5' #Wrong Letter
    yellow_square = '\U0001f7e8' #Correct Letter

    square_1, square_2, square_3, square_4, square_5 = red_square, red_square, red_square, red_square, red_square

    for i in range(len(guess)):
        if guess[i] in word:
            if i == 0:
                square_1 = yellow_square
            elif i == 1:
                square_2 = yellow_square
            elif i == 2:
                square_3 = yellow_square
            elif i == 3:
                square_4 = yellow_square
            elif i == 4:
                square_5 = yellow_square
            
            if guess[i] == word[i]:
                if i == 0:
                    square_1 = green_square
                elif i == 1:
                    square_2 = green_square
                elif i == 2:
                    square_3 = green_square
                elif i == 3:
                    square_4 = green_square
                elif i == 4:
                    square_5 = green_square
            

    squares = square_1 + square_2 + square_3 + square_4 + square_5
    
    return squares

def get_letters(guess, word):
    letters = []
    for i in range(len(guess)):
        if guess[i] in word:
            if guess[i] not in letters:
                letters.append(guess[i])

    letters.sort()

    return letters
#-------------------------------------------------------------------
def end_screen():
    clearScreen()
    print(
    """
    Thank you for playing!
    Wordinal (Wordle Clone)
    Created By: Nathaniel Macapinlac
    """
    )
#------------------------------------------------------------------
def main():
    print("Welcome to Wordinal! Would you like to play?")
    isPlaying()

if __name__ == '__main__':
    main()
