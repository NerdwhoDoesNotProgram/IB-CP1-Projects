# IB - Madlib

"""noun = input("Enter a noun: ").lower().strip()
animal = input("Enter an animal: ").lower().strip()
verb = input("Enter a verb: ").lower().strip()
adjective = input("Enter an adjective: ").lower().strip()
food = input("Enter a food: ").lower().strip()

story = "Yesterday, I found a " + adjective + " " + noun + " riding a " + animal + " down the street. "
story = story + "The " + animal + " suddenly decided to " + verb + " while carrying a giant plate of " + food + ". "
story = story + "I tried to stop the " + animal + ", but the " + noun + " yelled that everything was completely normal. "
story = story + "Then the " + animal + " continued to " + verb + " until it disappeared behind a tree."

print(story)"""

user_input = []
words = ["a noun", "an animal", "a verb", "an adjective", "a food"]

for i in words:
    data = input(f"Enter {i}: ").lower().strip()
    user_input.append(data)

noun = user_input[0]
animal = user_input[1]
verb = user_input[2]
adjective = user_input[3]
food = user_input[4]

story = f"Yesterday, I found a {adjective} {noun} riding a {animal} down the street." f"The {animal} suddenly decided to {verb} while carrying a giant plate of {food}." f"I tried to stop the {animal}, but the {noun} yelled that everything was completely normal." f"Then the {animal} coninued to {verb} until it dissapeared behind a tree."

print(story)