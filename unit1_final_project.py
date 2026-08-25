# IB - Interactive Introduction Program Code

name = input("What is your name? ").strip().title()

school = input("What school do you attend? ").strip()

hobby = input("What is your favorite hobby or activity? ").strip()

fav_genre = input("What is your favorite type of book, movie, or game? ").strip().capitalize()

dream_destination = input("What is a place you would like to visit someday? ").strip().title()

future_goal = input("What is something you would like to accomplish in the future? ").strip()

personality = input("Describe yourself using one word: ").strip().lower()

print(f"\nHi! My name is {name}, and I attend {school}. "
f"I would describe myself as {personality}. "
f"In my free time, I enjoy {hobby}, and I especially like {fav_genre}. "
f"One place I would love to visit is {dream_destination}, "
f"and one of my goals for the future is to {future_goal}. "
f"Thanks for getting to know me!")