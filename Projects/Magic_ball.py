""" A magic 8 ball game to display  random responses to a user's question"""

import tkinter
import random

responses = ["Nice question!", "I don't have an answer for you.", "wow! Amazing", "Why ask  me that?",
             "You don't want me to answer that!", "Don't be a weirdo.", "You must be a genius!", "Try using google!",
             "That's interesting", "Ask again!", "That's a simple question", "You can try again!",
             "I expected a better question!", "I don't have to prove i'm a genius!", "How do i know that?",
             "Try again!", "Never give up!", "Keep asking", "Next question?", "Maybe next time."]


def login():
    user_login = input("""Welcome to the Magic-8-Ball game by Vickie! Nice having you here.
     You can login to play or exit the game at your own time. Enter 
       1 ==> To login
       2 ==> To exit : """)
    if user_login == "1":
        username = input("Welcome again! Enter your preferred name: ")
        print("Hello", username)
        magic_ball()
    elif user_login == "2":
        print("Thank you for checking out!See you next time.")
        exit()
    else:
        print("Invalid command!")
        login()


def magic_ball():
    user_question = input('Please enter your question: ')
    answer = random.choice(responses)
    print("Thinking.........................................................")
    print("-"*100)
    print("Thanks for waiting, your answer is:", answer)
    next_question = input("Do you want to ask another question? Enter Yes or No : ")
    if next_question == "yes":
        magic_ball()
    elif next_question == "no":
        login()
    else:
        print("Please enter a valid command!")


login()
magic_ball()