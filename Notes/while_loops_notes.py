# IB - While Loops Notes

# A While loop keeps running until a condition is met

import random, time

goose = random.randint(1, 20)
duck = 1

while goose > duck:
    print("Duck...")
    time.sleep(0.2)
    duck += 1
    if duck == 15:
        print("Game over")
        break
else:  # Will only happen when your loop ends naturally. (Conditional becomes false) If you break out of a loop, it will not do the else at the bottom.
    print("GOOSE!")

# Start point: Variable outside the loop, generally. For example, the duck

# Second part: End point. (A boolean statement, for example, goose > duck)

# Third part: Incrementer. (duck += 1) The Incrementeris ised to change the itorator
    # An itorator is keeping track of the current itoratoin, or how many times the loop has run.

count = 30

while count > 0:
    print(count)
    time.sleep(0.1)
    count -= 1


number = random.randint(1, 101)

while True:
    while True:
        try:
            guess = int(input("\nGuess a number between 1 and 100: "))
            if guess < 0 or guess > 100:
                print('You shouldreas the instructions!')
                continue
            break
        except:
            print("That isn't a number")

    if guess == number:
        print(f"You win! The number was {number}!")
        break
    elif guess < number:
        print('That number is too low')
    elif guess > number:
        print("That number is too large.")
    else:
        print("I don't know how you got here... but you did something wrong")
# True is the start itself
# Break is the endpoint


# Key words
    # Break: Exits the loop
    # Continue: Starts the next iteration