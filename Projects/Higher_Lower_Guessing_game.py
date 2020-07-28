""" Welcome to the higher and lower guessing game. User is expected to either chose to play or exit the game. If user
chooses to play. User is expected to guess a number between 1 and 100 against the computer number, if the guess is
 correct the computer congratulates them and tell them how many  guesses they used"""

import random


def login_user():
    user_login = input("Enter 1 to play or 2 to exit: ")
    if user_login == '1':
        start_game()
    elif user_login == '2':
        exit()
    else:
        print('Wrong choice! chose either 1 or 2 to continue')
        login_user()


def start_game():
    guess_count = 0
    guess_limit = 5
    username = input('Please enter your name: ')
    print('Hello', username, '! welcome to the guessing game')
    while True:
        try:

            user_guess = int(input("Please guess a number: "))
            computer_number = random.randrange(1, 100)
            if user_guess < computer_number:
                print('Sorry your guess is low')
                guess_count += 1
            elif user_guess > computer_number:
                print('That guess was too high')
                guess_count += 1
            else:
                print('Correct! You are a star')
                print("You used", guess_count, "guesses.")
            if guess_count == guess_limit:
                print("The correct guess is", computer_number, "and you used", guess_count, "guesses")
                login_user()
        except ValueError:
            print('Oh there wrong input! Enter an integer')


login_user()
start_game()


