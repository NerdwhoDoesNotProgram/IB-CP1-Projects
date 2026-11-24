# IB - Maze Generator

# https://www.w3schools.com/dsa/dsa_algo_mst_prim.php

import random as r
import turtle as t

ROWS = 8
COLS = 8
CELL = 40
# size of each square in pixels
WALL_CHANCE = 0.35
# chance an extra cell becomes a wall

rows = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

columns = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def setup_screen():
    """Create the screen and the drawing turtle, and return them."""
    screen = t.Screen()
    screen.bgcolor("black")
    screen.screensize(1500, 1500)
    turtle = t.Turtle()
    turtle = t.hideturtle()
    return screen, turtle

def carve_path(grid):
    """Mark a path of 0s from the top-left to the bottom-right."""
    pass

def generate_maze():
    """Return a ROWS x COLS grid: 0 = path, 1 = wall."""
    pass

def draw_square(pen, x, y, color):
    """Draw one filled square with its top-left corner at (x, y)."""
    pass

def draw_maze(pen, grid):
    """Use nested loops to draw every cell in the grid."""
    for row in grid:
        for column in row:
            pass

def main():
    screen, pen = setup_screen()
    grid = generate_maze()
    draw_maze(pen, grid)
    screen.update()
    screen.mainloop()


main()