# IB, Random Numbers Notes

import random

ducks = random.randint(1, 10)  # Returns a random integer between 1 and 10 (inclusive)

print(f"There are {ducks} ducks!")

pens = random.randrange(1, 15, 3) # Randrange returns a randomly selected element from the range created by the arguments. In this case, it will return a random even number between 1 and 15 (inclusive of 1, exclusive of 15). The last 3 is the step, which means it will only consider numbers that are multiples of 3.
print(f"There are {pens} pens!")

percent = random.random()  # Returns a random float between 0.0 and 1.0 (inclusive of 0.0, exclusive of 1.0)
print(f"You have a {percent:.2%} grade.")  # Format as percentage with 2 decimal places