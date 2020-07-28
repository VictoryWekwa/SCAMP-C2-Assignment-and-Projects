""" A program that prints out every line of the song
    99 bottles of beer on the wall"""
# A while loop wil be used for this program
count = 99 # starting number of the game, setting it as my count
while count > 1:
    print(count, "bottles of beer on the wall", count,
          "bottles of beer on the wall, take one down and pass it around", count-1,
          "bottles of beer on the wall.")
    count -= 1
else:
    print(count, "bottle of beer on the wall", count, "bottle of beer on the wall, take one down"
                                                      "and pass it around, no more bottles of beer on the wall.")
print("Go to the store and buy some more", count+98, "bottles of beer on the wall.")




