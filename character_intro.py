# IB - Character Introduction

name = input("What is your character's name? ").strip().title()
age = input("How old is your character? ").strip()
job = input("What is your character's job? ").strip().lower()
hometown = input("Where is your character from? ").strip().title()

print(f"Hi, my name is {name}. I am {age} years old, I work as a {job}, and I'm from {hometown}.")