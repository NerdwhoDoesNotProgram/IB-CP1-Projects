# IB - Character Introduction Asignment

char_name = input("What is your character's name? ").strip().title()
char_age = input("How old is your character? ").strip()
char_job = input("What is your character's job? ").strip().lower()
char_hometown = input("Where is your character from? ").strip().title()

print(f"Hi, my name is {char_name}. I am {char_age} years old, I work as a {char_job}, and I'm from {char_hometown}.")