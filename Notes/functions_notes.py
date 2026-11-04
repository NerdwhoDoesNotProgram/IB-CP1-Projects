# IB - Funcitons Notes

"""
# Function: a named block of code that does one job and can be used (called) whenever you need it

# Built-in vs. user-defined: built-in functions like print(), len(), and input() come with Python. User-defined functions are the ones you write yourself with def.

    # Readability: a good function name tells the reader what a chunk of code does without making them read every line

    # Reusability: write the code once, then call it as many times as you want instead of copying and pasting

    # Modularity: breaking a big program into small, separate pieces that each do one job

    # Abstraction: you can use a function without knowing how it works inside. You only need to know what it does and what it needs.

# Parameters vs. arguments: a parameter is the variable name in the function definition. An argument is the actual value you pass in when you call the function.

# Return: sends a value back to the place the function was called. Without a return, a function gives back None.

# Scope: the part of a program where a variable can be used

# Local variable: created inside a function, and only exists while that function runs

# Global variable: created outside all functions, and can be seen anywhere in the file

# Functions may or may not take arguments, and may or may not return a value
"""
"""Order:
Global variables
Functions
Main code"""



def birthday(name, age=35):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")
    print("Happy Birthday to you\n")
    print(f"You are now {age} years old!")
  
def main():
    name = input("Tell me your name: ")

    print("November")
    birthday("Tia", 30)

    print("December")
    birthday("Xavier", 24)

    print("January")
    birthday("Treyson", 20)

    birthday(name)

#main()

"""------------------------------------------------------------------------------------------------"""
# Day two of functions notes

"""Takes in a question, tata type, correct answers (Default as an empty list)
    
    input within function, and then check fo data type."""

"""For commenting on funcitons you do the three qutaotpnmarks after the name line, and hten describe the funciotn"""

attempts = 0

def stupid_proof(user_answer, correct_answers):
    user_answer = user_answer.strip().lower()
    if user_answer in correct_answers:
        return True, user_answer, increase()
    else:
        return False, user_answer, increase()
    
def increase():
    return attempts +1

while True: 
    capital = input("What is the capital of Utah: ")

    correct, capital, attempts = stupid_proof(capital, ["salt lake city", "slc", "salt lake", ])

    if correct:
        print(f"Good job {capital} is the capital of Utah!")
        break
    else: 
        print(f"Try again. {capital} is not the capital of Utah. You have tried {attempts} time(s).")