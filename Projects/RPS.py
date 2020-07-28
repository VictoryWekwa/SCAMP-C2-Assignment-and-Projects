""" A Rock, Paper, Scissors game. The player is expected to pick from rock, paper, or scissor
and the computer is expected to pick its move.
A list was created to store the options and the choice in the random module is used so that the computer can
display it's choice.If the option chosen by the user is the same with that of the computer the user win but if it is not
the computer wins.
"""

import random
options = ['rock', 'paper', 'scissors']


def game_now():
    player_score = 0
    computer_score = 0

    player = input('Chose between rock, paper or scissor: ')
    computer_choice = random.choice(options)
    if computer_choice == player:
        print('User win')
        player_score += 1
    elif computer_choice != player:
        print('Computer wins')
        computer_score += 1
    final_scores = computer_score, player_score
    play_option = input('Do you want to play again? Enter yes or no: ')
    if play_option == 'yes':
        game_now()
    elif play_option == 'no':
        print('Computer choice is', computer_choice)
        print('The final results is:', final_scores)


game_now()