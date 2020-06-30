""" A function that allows the user to check whether a given number is armstrong or not,
first determine the number of digits in the given number and call that n, then take every digit in the number
and raise it  to the nth term, Add them and if the answer gives the original number then it is an armstrong
Also note that all single digits are armstrong"""


def armstrong():
    try:
        user_number = input("Please enter a number: ") # user inputs any number of their choice
        n = len(user_number) # Getting the len of the number using len since i collected the number as a string
        final_answer = 0  # Setting my final expected result to zero i see it more as a counter
        user_number_int = int(user_number) # Converting my initial user number collected as a string to an integer
        for v in range(0, n): # simply means for value in the range starting from 0 to the len of my user_number
            final_answer = final_answer + (int(user_number[v])**n) # updating the final result set as zero initially
        if final_answer == user_number_int:
            print("Yay! Your number is an armstrong")
        else:
            print("Oh sorry!Try again")
    except ValueError:
        print("Please enter an integer and try again.")


armstrong()