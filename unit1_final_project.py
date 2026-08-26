# IB - Interactive Introduction Program Code

name = input("What is your name? ").strip().title()

school = input("What school do you attend? ").strip() #title does not work for acronyms such as UCAS

hobby = input("What is your favorite hobby or activity? ").strip() # lowercase?

fav_genre = input("What is your favorite type of book, movie, or game? ").strip().capitalize()

dream_destination = input("What is a place you would like to visit someday? ").strip().title()

future_goal = input("What is something you would like to accomplish in the future? ").strip()

personality = input("Describe yourself using one word: ").strip().lower()

"""print(f"\nHi! My name is {name}, and I attend {school}. I would describe myself as {personality}. In my free time, I enjoy {hobby}, and I especially like {fav_genre}. One place I would love to visit is {dream_destination}, and one of my goals for the future is to {future_goal}. Thanks for getting to know me!")"""

# Having separate f strings make writing, editing, and structuring of sentences much easier.
print(f"\nHi! My name is {name}, and I attend {school}. "
f"I would describe myself as {personality}. "
f"In my free time, I enjoy {hobby}, and I especially like {fav_genre}. "
f"One place I would love to visit is {dream_destination}, "
f"and one of my goals for the future is to {future_goal}. "
f"Thanks for getting to know me!")
