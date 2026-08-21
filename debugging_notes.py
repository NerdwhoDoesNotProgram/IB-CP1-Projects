# IB Debugging Notes

# Syntax Error
"""print("Hello)
      
# Indentation error
if True:
print("This is true") # <= indentation error

people = 10
print(poeple)"""

# Logic Error
# read code again
"""apples = 20
people = 3

print(apples*people)"""
"""print(apples//people)"""
# Run-time Errors
"""fav_num = input("What is your favorite number")

print(4 + fav_num)"""

# Input validaiton
while True:
    try:
        fav_num = int(input("What is your favorite number: "))
    except:
        print("That's not a number!")
    else:
        break

print(4 + fav_num)