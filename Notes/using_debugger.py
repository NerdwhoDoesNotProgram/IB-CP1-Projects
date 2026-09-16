# IB - Using the Debugger

# Play button: Continue. This continues the program until it reaches the next breakpoint or         finishes execution. (F5)

# Step over button: This executes the current line of code and moves to the next line in the same function. (F10)

# Step into button: This goes into the function call on the current line and allows you to debug inside that function. (F11)

# Step out button: This executes the rest of the current function and returns to the calling function. (shift + F11)

# Restart button: This restarts the program from the beginning. (ctrl + shift + F5)

# Stop button: This stops the program execution. (shift + F5)

# Watch screen: This allows you to monitor the values of variables as you step through the code. You can add variables to the watch screen to see how their values change during execution.

# Most importantly, the debugger is your best friend.



scores = [12, 45, 7, 68, 33, 90, 21,]

running_total = 0
highest_score = 0

for score in scores:
    running_total += score
    if score > highest_score:
        highest_score = score


"""grades = [85, 90, 78, 92, 88]

total = 0
count = len(grades)

for grade in grades:
    total += grade

average = total / count

print(f"The average grade is: {average}")"""

