# IB, 2nd period - Condiitonal Notes

grade = int(input("What is your grade in the class: "))

if grade >= 90:
    print("You have an A in the class!")
elif grade >= 70:
    print("You are passing the class!")
else:
    print("You are failing the class.")
    print("You might need ot retake a quiz, or submiyt a missing assignment.")

"""username = input("What is your username: ").strip()

if bool(username):
    print("You diedn't enter a username.")
elif username == "LaRose":
    print("You are a Teacer :)")
else:
    print("You are a student.")"""

raining = False

if not raining:
    print("Wear sunscreen")
else:
    print("Bring an umbrella")