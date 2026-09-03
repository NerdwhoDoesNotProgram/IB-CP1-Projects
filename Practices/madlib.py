# IB - Madlib

# IB, Period __, Madlib Assignment

noun = input("Enter a noun: ").lower().strip()
animal = input("Enter an animal: ").lower().strip()
verb = input("Enter a verb: ").lower().strip()
adjective = input("Enter an adjective: ").lower().strip()
food = input("Enter a food: ").lower().strip()

story = "Yesterday, I found a " + adjective + " " + noun + " riding a " + animal + " down the street. "
story = story + "The " + animal + " suddenly decided to " + verb + " while carrying a giant plate of " + food + ". "
story = story + "I tried to stop the " + animal + ", but the " + noun + " yelled that everything was completely normal. "
story = story + "Then the " + animal + " continued to " + verb + " until it disappeared behind a tree."

print(story)