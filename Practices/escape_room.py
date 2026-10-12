# IB - Escape room

import random

code = 1234
hints = ("Hint1", "Hint 2", "Hint 3", "Hint 4")
tries = 0
hint_number = 3
room_description = ""

"""
while True:
    while True:
        try:
            guess = int(input("\nGuess the passcode: "))
            if guess < 0 or guess > 100:
                print('You should read the instructions!')
                continue
            break
        except:
            print("That isn't a number")

    if guess == code:
        print(f"You win! The number was {code}!")
        break
    elif guess < code:
        print('That number is too low')
    elif guess > code:
        print("That number is too large.")
    else:
        print("I don't know how you got here... but you did something wrong")
"""

while tries < 4:
    while True:
        try:
            guess = int(input("\nWhat is the password: "))
            break
        except:
            print("That is not avalid form of the code. Please try again.")

    if guess == code:
        print("You Escaped!")
        break
    else:
        print(f"Hint: {hints[hint_number]}")
        hint_number -= 1
        tries += 1

print('You are trapped')
