# IB - Turtle race

# https://docs.python.org/3/library/turtle.html#turtle-state

import turtle as t
import random
import time

# Pseudocode:
"""
# Set up the screen and finish line
# Ask the user to choose a turtle color
# Give the user's turtle that color
# Give the other turtles different colors
# Place all turtles at the starting line
# Start the timer
# While nobody has won:
#     Move each turtle a random number of steps
#     Check if a turtle crossed the finish line
# Announce the winner and race time
# Tell the user if their turtle won"""

# Function that draws the finish line
def drawline(X):
    line = t.Turtle()
    line.pencolor("white")
    line.speed(0)
    line.hideturtle()
    line.penup()
    line.goto(X, 250)
    line.pendown()
    line.goto(X, -250)

# Function that sets up the race
def setup_race():
    screen = t.Screen()
    screen.bgcolor("black")
    screen.title("Turtle Race!")
    screen.setup(800, 600)

    # Draw finish line
    drawline(300)
    drawline(320)

    # Ask user to choose a color
    colors = ["red", "blue", "green", "orange",
              "purple", "yellow", "cyan", "pink"]

    player_color = input("Choose your turtle color: " ).lower()

    while player_color not in colors:
        print("That color is not available.")
        player_color = input("Choose red, blue, green, orange, purple, yellow, cyan, or pink: ").lower()

    # Choose different colors for the other turtles
    other_colors = colors.copy()
    other_colors.remove(player_color)
    other_colors = random.sample(other_colors, 4)

    # Create turtles
    racers = []
    all_colors = [player_color] + other_colors

    for i in range(5):
        racer = t.Turtle()
        racer.shape("turtle")
        racer.color(all_colors[i])
        racer.penup()
        racer.goto(-350, 200 - (i * 100))
        racers.append(racer)

    return screen, racers, player_color

# Function that moves turtles
def move_turtles(racers):
    for racer in racers:
        racer.forward(random.randint(1, 10))

# Function that finds the winner
def find_winner(racers):
    for racer in racers:
        if racer.xcor() >= 300:
            return racer

    return None

# Function that runs the race
def run_race():
    screen, racers, player_color = setup_race()

    start = time.time()
    winner = None

    while winner == None:
        move_turtles(racers)
        winner = find_winner(racers)

    race_time = round(time.time() - start, 2)
    winner_color = winner.pencolor()

    print("The " + winner_color + " turtle won!")
    print("Race time:", race_time, "seconds")

    if winner_color == player_color:
        print("Congratulations! Your turtle won!")
    else:
        print("Sorry! Your turtle did not win.")

    # Display winner on screen
    message = t.Turtle()
    message.color("white")
    message.hideturtle()
    message.penup()
    message.goto(0, -250)
    message.write("The " + winner_color + " turtle won!",
                  align="center", font=("Arial", 20, "bold"))

    message.goto(0, -280)
    message.write("Race Time: " + str(race_time) + " seconds",
                  align="center", font=("Arial", 14, "normal"))

    screen.exitonclick()

# Calls the function that runs the race
run_race()