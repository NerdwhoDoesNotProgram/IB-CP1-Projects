# IB - Fix the Game

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)

    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number: # The code was missing the ending colon, which is a Syntax eror. This does not allow the code to run because it does not signal for the contents of the if statement.
            print(f"Correct! It took you {guesses} guesses.\n")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
#print("Your guesses per round: " + scores)
print(f"Your guesses per round: {scores}") # This is a Runtime error, where the 0cde tries to cacatanate the string to the list, which it can't do. To fix this, we use an F string to displays scores instead.

total = 0
for score in scores:
    #total = 0  # Removed this line, because each itteratoin, it reset the total variable. This is a Logic error.
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(round(average, 2))) # I don't think this is an error, but this now rounds the avarage guesses.

best_round = scores[0]
for i in range(rounds): # Since range is exclusibe, it not use the last index of the list.  This would be a Runtime error.
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")