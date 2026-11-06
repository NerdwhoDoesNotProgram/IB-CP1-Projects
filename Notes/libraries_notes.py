# IB - Library Notes

"""
Library: a collection of pre-written code (mostly functions) that you can bring into your own program instead of writing it yourself
Import: the statement that brings a library into your program. It goes at the top of your file, for example import math.
Built-in function: a function that comes with Python and is ready to use, like print(), input(), and len(). No import is needed.
Library function: a function that lives inside a library. You have to import the library first, then call it with the library's name, like math.sqrt(16).
User-defined function: a function you write yourself with def
Argument: a value you give to a function when you call it, like the 16 in math.sqrt(16)
Void return: a function that does its job but doesn't hand back a value (it returns None). Turtle's forward() is an example.
Why use libraries? They save time, they are already tested, and they let you do big things (graphics, math, randomness) with very little code
Turtle: a library that lets you draw by giving commands to a "turtle" that moves around the screen"""

# import turtle
# from turtle import *
import turtle as t  # Doing as t is called ailising, making it eaier to write

t.exitonclick()
t.shapesize()
(1.0, 1.0, 1)
t.resizemode("user")
t.shapesize(5, 5, 12)
t.shapesize()
(5, 5, 12)
t.shapesize(outline=8)
t.shapesize()
(5, 5, 8)


#t.showturtle()
t.forward(250)
t.left(120)
t.forward(100)
t.left(120)
t.forward(120)
t.up()
t.goto(40, 80)
t.down()
t.forward(200)