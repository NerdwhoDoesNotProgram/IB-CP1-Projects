# IB, 2nd period - Madlib

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

words = [
    "a name",
    "an adjective",
    "a funny object",
    "a plural noun",
    "a verb",
    "a place",
    "a body part",
    "an adjective",
    "a verb ending in -ing",
    "an exclamation or silly word",
    "a number",
    "a liquid"
]

for i in words:
    data = input(f"Enter {i}: ").lower().strip()
    user_input.append(data)

name = user_input[0]
adjective1 = user_input[1]
noun_object = user_input[2]
plural_noun = user_input[3]
verb = user_input[4]
place = user_input[5]
body_part = user_input[6]
adjective2 = user_input[7]
verb_ing = user_input[8]
exclamation = user_input[9]
number = user_input[10]
liquid = user_input[11]

story = f"Attention students! The race for Student Council President is heating up, and today {name.title()} gave a truly {adjective1} speech in the auditorium. {name.title()} promised that if elected, they would replace all classroom chairs with a comfortable {noun_object}. The crowd of {plural_noun} began to {verb} with excitement while the principal rushed onto the stage at {place} to restore order, but accidentally slipped on a banana peel and injured his {body_part}. Suddenly, things got completely {adjective2} when a group of mascot-costumed students started {verb_ing} down the aisles, shouting \"{exclamation.capitalize()}!\" In the end, the voters were given {number} juice boxes filled with {liquid}, and {name.title()} won the election thanks to the magical power of the campaign {noun_object}!"

print(story)


"""story = f"Yesterday, I found a {adjective} {noun} riding a {animal} down the street." f"The {animal} suddenly decided to {verb} while carrying a giant plate of {food}." f"I tried to stop the {animal}, but the {noun} yelled that everything was completely normal." f"Then the {animal} coninued to {verb} until it dissapeared behind a tree."""