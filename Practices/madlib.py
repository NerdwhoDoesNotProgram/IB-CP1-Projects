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
words = ["a noun", "an animal", "a verb", "an adjective", "a food"]

for i in words:
    data = input(f"Enter {i}: ").lower().strip()
    user_input.append(data)

noun = user_input[0]
animal = user_input[1]
verb = user_input[2]
adjective = user_input[3]
food = user_input[4]

"""story = f"Yesterday, I found a {adjective} {noun} riding a {animal} down the street." f"The {animal} suddenly decided to {verb} while carrying a giant plate of {food}." f"I tried to stop the {animal}, but the {noun} yelled that everything was completely normal." f"Then the {animal} coninued to {verb} until it dissapeared behind a tree."""

story = f"Attention students! The race for Student Council President is heating up, and today {Noun Title} gave a truly {Adjective} speech in the auditorium. They promised that if elected, they would replace all classroom chairs with a comfortable {Noun Object}.The crowd of {Plural Noun} began to {Verb} with excitement! The principal rushed onto the stage of the {Noun Place} to restore order, but accidentally slipped on a stray banana peel, injuring his {Body Part}.Suddenly, things got completely {Adjective}. A group of mascot-costumed students started {Verb_ing} down the aisles. {Exclamation}! shouted the crowd.In the end, the voters were given {Number} juice boxes filled with {Liquid} to calm down. It turns out that {Noun Title} won the election by a landslide, all thanks to the magical power of the campaign {Noun Object}!"

print(story)

"""Noun (a person's title, e.g., Captain, Doctor, Queen): ________________________ (Used twice!)Adjective: ________________________Noun (a funny object): ________________________ (Used twice!)Plural Noun: ________________________Verb (action): ________________________Noun (Place): ________________________Body Part: ________________________Adjective: ________________________Verb ending in "-ing": ________________________Exclamation / Silly Word: ________________________Number: ________________________Liquid: ________________________Step 2: The StoryPlug your words into the numbered blanks below to reveal the chaos of a school election campaign gone off the rails!Attention students! The race for Student Council President is heating up, and today [1. Noun Title] gave a truly [2. Adjective] speech in the auditorium. They promised that if elected, they would replace all classroom chairs with a comfortable [3. Noun Object].The crowd of [4. Plural Noun] began to [5. Verb] with excitement! The principal rushed onto the stage of the [6. Noun Place] to restore order, but accidentally slipped on a stray banana peel, injuring his [7. Body Part].Suddenly, things got completely [8. Adjective]. A group of mascot-costumed students started [9. Verb ending in "-ing"] down the aisles. "[10. Exclamation]!" shouted the crowd.In the end, the voters were given [11. Number] juice boxes filled with [12. Liquid] to calm down. It turns out that [1] (Noun Title) won the election by a landslide, all thanks to the magical power of the campaign [3] (Noun Object)!"""