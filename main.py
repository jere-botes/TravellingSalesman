# JBC MEDIA | Travelling salesman problem | MAR 2018 | v1.9 | Jere Botes

# ---------------------------------------------------------------------------
# MODULES & OPTIONS
# ---------------------------------------------------------------------------
import turtle
import math
import random
import time
import datetime
from itertools import *
import winsound
from winsound import PlaySound, SND_FILENAME, SND_ASYNC

# ---------------------------------------------------------------------------
# SCREEN / WINDOW SETUP
# ---------------------------------------------------------------------------
wn = turtle.Screen()
wn.bgcolor('black')
wn.title("TSP - Travelling Salesman Problem - Input Manual Coordinates")

scr_width = 1200
scr_height = 800

wn.setup(scr_width, scr_height)
turtle.delay(0)
wn.tracer(0)

# ---------------------------------------------------------------------------
# DRAW SCREEN GRID
# ---------------------------------------------------------------------------
line = turtle.Turtle()
line.color("#444")
line.shape("square")
line.shapesize(0.1, 0.1)
line.speed(0)
line.hideturtle()
line.pensize(1)

bl = turtle.Turtle()
bl.color("blue")
bl.speed(0)
bl.hideturtle()
bl.pensize(3)
sq_side = 25

def draw_square():
    for x in range(4):
        line.pendown()
        line.forward(sq_side)
        line.right(360/4)
        line.stamp()
        line.penup()

# start grid layout point
start_x = scr_width/2 * -1
start_y = scr_height/2

line.penup()

y_go = start_y
while y_go > scr_height/2 * -1:
    x_go = start_x
    while x_go < scr_width/2:
        line.goto(x_go, y_go)
        draw_square()
        x_go += sq_side

    y_go -= sq_side

bl.pendown()
bl.goto(0, scr_height/2 * -1)
bl.setheading(90)
bl.forward(scr_height)

bl.penup()
bl.goto(scr_width/2 * -1, 0)
bl.setheading(0)
bl.pendown()
bl.forward(scr_width)

# ---------------------------------------------------------------------------
# DRAW POLYGONS
# ---------------------------------------------------------------------------
wn.update()

write_txt = turtle.Turtle()
write_txt.speed(0)
write_txt.color("white")
write_txt.penup()
write_txt.setposition(-590, 380)
write_txt.hideturtle()

write_m = turtle.Turtle()
write_m.speed(0)
write_m.color("white")
write_m.penup()
write_m.setposition(-500, 360)
write_m.hideturtle()

nr_points = int(wn.numinput("Nr of nodes?", "How many nodes would you like to brute force?", minval=3, maxval=12))
txt1 = "Click anywhere on the screen to start pathfinding process..."
txt2 = nr_points
txt3 = " points remaining"
textstring = txt1, txt2, txt3
write_txt.clear()  # clear old score before writing new
write_txt.write(textstring, False, align="left", font=("Arial", 10, "bold"))

# ---------------------------------------------------------------------------
# SETUP THE SPRITES
# ---------------------------------------------------------------------------
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.speed(0) # Fastest
        self.hideturtle()

draw = Pen()
draw.color("yellow")
draw.speed(0)

# ---------------------------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------------------------
def get_mouse_coords(x, y):
    xclick = int(x)
    yclick = int(y)
    print(xclick, yclick)
    draw.goto(xclick, yclick)
    draw.stamp()

    if len(coordinates) < nr_points:
        coordinates.append((xclick, yclick))
        print(coordinates)

        txt1 = nr_points - len(coordinates)
        txt2 = "nodes remaining..."
        textstring = txt1, txt2
        write_txt.clear()  # clear old score before writing new
        write_txt.write(textstring, False, align="left", font=("Arial", 10, "bold"))

    if len(coordinates) == nr_points:
        # if all nodes clicked, write the text file
        with open("coords.txt", "w") as output:
            output.write(str(coordinates))

        print("Thanks, ",nr_points,"coordinates saved!")

        draw.color("black")
        textstring = "Ok, " + str(nr_points) + " coordinates was saved successfully!"
        write_txt.clear()  # clear old score before writing new
        write_txt.write(textstring, False, align="left", font=("Arial", 10, "bold"))
        write_txt.clear()  # clear old score before writing new

        import tsp_brute_force
        #exit()


def click_point():
    turtle.onscreenclick(get_mouse_coords)

# ---------------------------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------------------------
coordinates = []
click_point()
turtle.done()







