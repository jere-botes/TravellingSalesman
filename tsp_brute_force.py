# JBC MEDIA | TSP - THE TRAVELLING SALESMAN PROBLEM | BRUTE FORCE MANUAL FINDER| MAR 2018

# -------------------------------------------------------
# MODULES & OPTIONS
# -------------------------------------------------------
import turtle
import math
import random
import time
import datetime
from itertools import *
import winsound
from winsound import PlaySound, SND_FILENAME, SND_ASYNC

# -------------------------------------------------------
# SCREEN / WINDOW SETUP
# -------------------------------------------------------
wn = turtle.Screen()
wn.bgcolor('black')
wn.title("Jere's TSP - Travelling Salesman Problem - Brute force shortest path finder")
wn.setup(1200, 800)
turtle.delay(0)
wn.tracer(0)

# ---------------------------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------------------------

# euclidean distance // pythagorean theorem | c = square root of a2 + b2
def distance_from(point_a, point_b):
    a = int(point_a[0]) - int(point_b[0])
    b = int(point_a[1]) - int(point_b[1])
    distance = math.sqrt((a ** 2) + (b ** 2))
    distance = int(round(distance, 0))
    return distance


def get_mouse_coords(x, y):
    # Make nice round integers without decimals
    xclick = int(x)
    yclick = int(y)
    print(xclick, yclick)
    draw.goto(xclick, yclick)
    draw.stamp()

    if len(coordinates) <= nr_points-1:
        coordinates.append((xclick, yclick))
        print(coordinates)


def click_point():
    turtle.onscreenclick(get_mouse_coords)



# ---------------------------------------------------------------------------
# SETUP THE SPRITES
# ---------------------------------------------------------------------------


# SETUP PEN CLASS
class Pen(turtle.Turtle):
    def __init__(self): # Initialize the Pen class (a child of turtle)
        turtle.Turtle.__init__(self) # Also initialize the turtle
        self.shape('circle')
        #self.shapesize(1, 1)
        self.color('green')
        self.penup()
        self.speed(0) # Fastest
        self.hideturtle()


# CREATE CLASS INSTANCES
draw = Pen()
draw.color("green")
draw.speed(0)

# -----------------------------------------------------

# Create the points turtle
node = turtle.Turtle()
node.color("black")
node.shape("circle")
node.speed(0)
node.penup()

# Create a line draw turtle
line = turtle.Turtle()
line.color("gray")
line.shape("circle")
line.speed(0)
line.penup()
line.hideturtle()

# Screen write points
write = turtle.Turtle()
write.speed(0)
write.color("white")
write.penup()
write.hideturtle()

# xcoord screen display
write_txt = turtle.Turtle()
write_txt.speed(0)
write_txt.color("white")
write_txt.penup()
write_txt.setposition(-500, 380)
write_txt.hideturtle()

# Create test points turtle
test_node = turtle.Turtle()
test_node.color("magenta")
test_node.shape("circle")
test_node.speed(0)
test_node.penup()
test_node.pensize(1)
test_node.hideturtle()

# Create solution turtle
solution = turtle.Turtle()
solution.color("light green")
solution.shape("square")
solution.speed(0)
solution.pensize(10)
solution.hideturtle()

write_m = turtle.Turtle()
write_m.speed(0)
write_m.color("yellow")
write_m.penup()
write_m.setposition(-500, 360)
write_m.hideturtle()

# ---------------------------------------------------------------------------
# GENERATE RANDOM POINTS - coordinates list
# ---------------------------------------------------------------------------
coordinates = []
ext_file = "coords.txt"
string = open(ext_file).read()
string = string[1:-1]
string = string.replace("), (", ")*(")
manual_coords = string.split("*")

for node in manual_coords:
    node = node[1:-1]
    manual = node.split(", ")
    man_x = int(manual[0])
    man_y = int(manual[1])
    coordinates.append((man_x, man_y))

point_zero = coordinates[0]


# ---------------------------------------------------------------------------
# NR OF POINTS & INFO
# ---------------------------------------------------------------------------
nr_points = len(coordinates)

# Possible paths from (1st point only, so we divide the factorial by nr of points again)
pos_pa = int(math.factorial(nr_points) / nr_points)

# Estimated time to compute (Taken @ about 39000 iterations per second)
est_time = round(pos_pa/32000, 1)

# Start time
date = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
start_time = time.time()


# ---------------------------------------------------------------------------
# WRITE INFO TO SCREEN
# ---------------------------------------------------------------------------
txt1 = "Travelling Salesman - Nodes to visit: %s" % nr_points
txt2 = "Path possibilities: %s" % pos_pa
txt3 = "Estimated time to solution: %s" % est_time
txt4 = "seconds...  |  Start: %s" % date
textstring = txt1, txt2, txt3, txt4
write_txt.clear()  # clear old score before writing new
write_txt.write(textstring, False, align="left", font=("Arial", 10, "normal"))

# ---------------------------------------------------------------------------
# LOOP TO CREATE A LIST OF POSSIBLE PERMUTATIONS
# ---------------------------------------------------------------------------

permutation_list = []
curr_cor = 0
for coord in coordinates:
    next_point = 0
    for i in range(nr_points):
        dist = distance_from(coord, coordinates[next_point])
        next_point = next_point + 1

    permutation_list.append(coord)
    curr_cor = curr_cor + 1

print("Permutation list created successfully...")
print("Point zero is: ", point_zero)

# ---------------------------------------------------------------------------
# TRY EACH PERMUTATION AND CREATE A LIST OF DISTANCES FOR EACH PERMUTATION
# ---------------------------------------------------------------------------
path_distance_sums = []
single_lengths = nr_points
best_path = 100000
try_nr = 0

for iteration in (permutations(permutation_list, nr_points)):
    if iteration[0] == point_zero:

        # Print only at n increments to improve performance
        increments = 10000
        if (try_nr % increments == 0):
            print("Iter: ", try_nr)
            txt1 = "Appx. route iterations tried: %s" % try_nr
            txt2 = "Total possibilities: %s" % pos_pa
            txt3 = "Progress: %s" % round(try_nr/pos_pa*100, 2)
            txt4 = "%"
            textstring = txt1, txt2, txt3, txt4
            write_m.clear()  # clear old score before writing new
            write_m.write(textstring, False, align="left", font=("Arial", 10, "normal"))

        # reset path distance list
        path_distances = []

        # set 2nd coordinate as previous point to start loop with
        next_in_array = 1

        for pnt in iteration:
            next_point = iteration[next_in_array]
            dist = distance_from(next_point, pnt)
            path_distances.append(dist)
            next_in_array = next_in_array + 1
            if next_in_array == single_lengths:
                next_in_array = 0

    this_path_tot_dist = sum(path_distances)

    if this_path_tot_dist < best_path:
        best_path = this_path_tot_dist
        best_iteration = iteration
    else:
        best_path = best_path

    try_nr = try_nr + 1

# ---------------------------------------------------------------------------
# OUTPUT DATA
# ---------------------------------------------------------------------------
print("NODES: ", nr_points)
print("POSSIBLE PATH ITERATIONS TESTED: ", pos_pa)
print("SHORTEST ROUTE: ", best_path)

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("Found in ", total_time, "Seconds")


# ---------------------------------------------------------------------------
# DRAW THE SHORTEST PATH (SOLUTION)
# ---------------------------------------------------------------------------
print("SOLUTION: ")
wn.tracer(1)
solution.penup()
for pt in best_iteration:
    print(pt)
    solution.goto(pt)
    solution.stamp()
    solution.pendown()

solution.goto(best_iteration[0])
turtle.done()








