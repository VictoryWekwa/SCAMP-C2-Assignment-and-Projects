import statistics


def mean_number(array):
    mean_Number = statistics.mean(array)
    if array:
        # deciml_places = int(input("How many decimal places do you need? "))
        print("the mean is :", mean_Number)
    else:
        print("Enter a list of numbers")


def median_number(array):
    median_Number = statistics.median(array)
    if array:
        print("The median of the number is: ", median_Number)
    else:
        print("Invalid command!")


def mode_number(array):
    modal_Number = statistics.mode(array)
    if modal_Number >= 1:
        print("The mode of the list of the number is : ", modal_Number)
    else:
        print("Invalid command")


mean_number([2, 4, 5, 6, 8, 9, 0])
median_number([2, 4, 5, 6, 8, 9, 0, 3, 4, 7, 8, 9, 3])
# mode_number([2, 4, 5, 6, 8, 9, 0, 9, 7, 5, 6, 4])



