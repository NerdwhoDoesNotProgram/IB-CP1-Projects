# IB - For Loops Notes

import time

siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]

#    Iterator varable: common names include i, x, or single version of list name.
#     /        # Tell what list it is looking at
for sibling in siblings:
    print(f"Good morning {sibling}!")

grades = [100, 87, 53, 45, 78, 72, 88, 3, 94]
avarage = 0

for grade in grades:
    avarage += grade
    print(f"{grade} was added.")

avarage = avarage/len(grades)
print(f"The avarage grade is {avarage:.2f}")

#         With range, first number is where you start, ad the second is where you end (nit including that nubmer), and the last number is what it counts by (the iterator). If you just have one number, it starts at 0, and counts by one ot that number.
#         / 
for i in range(2, 21, 2): # This is technically a Boolean statement, because it is while true, or within the range. When the condiytionfails, the loop stops automatically.
    print(i)
    time.sleep(0.5)

for i in range(20, 0, -1):
    print(i)
    time.sleep(0.5)
    if i == 12:
        print("Wait, it is lunch time")
        break



"""
# Iteration: going through a collection of items one at a time, repeating the same action for each one

# For Loop: a loop that repeats code once for each item in a sequence (like a list) — used when you know what you're looping over

# Iterator variable: the variable that holds the current item during each pass through the loop — commonly named i, but can (and often should) be named something more descriptive, like color when looping over a list of colors

    * Indentation after the colon tells Python which lines are inside the loop (and will repeat) versus which lines come after the loop and only run once, after it finishes — same rule as with conditionals

# Repetition: running the same block of code more than once — loops are how programs repeat actions without copying and pasting the same code over and over

# Met Condition: when a loop's condition evaluates to true, allowing it to continue or begin another pass

# Failed Condition: when a loop's condition evaluates to false, which is what causes the loop to stop

# Exit Condition: the condition that determines when a loop stops running — for a for loop, this is simply running out of items to iterate over
"""