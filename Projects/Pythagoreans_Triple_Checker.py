""" A pythagoras triple is a set of three positive integers namely a, b, and c.
They represents the sides of a right triangle such that a^2 + b^2 = c^2.
This program is to check if a triangle is a pythagoras triple or not.
The user is expected to enter the sides of the the given triangle"""


def pythagoras_triple_checker():
    try:
        a = int(input('Enter the first side: '))
        b = int(input('Enter the second side: '))
        c = int(input('Enter the third side: '))

        if ((a**2)+(b**2)) == c**2 and a > 0 and b > 0 and c > 0:
            print('The triangle is a pythagoras triple')
        elif a < 0 and b < 0 and c < 0:
            print('Enter a positive Integer!')
        else:
            print('Not a pythagoras triple!')
    except ValueError:
        print('Invalid Command! Enter an integer!')


pythagoras_triple_checker()