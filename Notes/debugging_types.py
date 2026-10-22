# IB - Debugging types notes

import random

index = random.randint(0, 7)

siblings = ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake"]


print(siblings[index])





"""
# Read the error message first. Python tells you the exact line and the type of error (e.g. TypeError, NameError) — this is often the fastest strategy of all, and it's free. Don't skip straight to guessing.

# Print Debugging: add temporary print() statements to display a variable's value or confirm a line was reached. Best for quickly checking one or two suspicious variables.

# Using the Debugger: set a breakpoint and step through your code, watching every variable at once. Best for complex bugs involving several variables, or when you need to trace exactly when a value changes.

# Rubber Duck Debugging: explain your code out loud, line by line, to someone (or something) else. Best for logic errors, especially when you're not even sure what's wrong yet.

# Isolating the Bug: temporarily comment out or remove sections of your code until the bug disappears — whatever you just removed is where the problem lives. Best for narrowing down a bug in a long program when you don't know where to start looking.

# Reproducing the Bug: figure out the exact steps or inputs that cause the bug every time. Best for bugs that only happen "sometimes" — you can't fix what you can't reliably make happen again.

# Tracing by Hand: work through your code on paper, line by line, writing down what each variable equals as you go — like being the computer yourself. Best for logic errors in a short section of code.

# Testing with Simple Inputs: try your program with the simplest possible input (like 0, 1, or an empty string) instead of realistic data. Best for narrowing down whether a bug is in your core logic or just an edge case.

# Searching Documentation or the Web: look up the exact error message or function name. Best for unfamiliar errors or when you're not sure a function works the way you think it does. (W3schools, GeeksforGeeks)

# asking for Help / Code Review: have a classmate or teacher read your code. Best for when you've tried everything else and are too close to your own code to see the problem — a fresh set of eyes catches things you've stopped noticing.
"""

 