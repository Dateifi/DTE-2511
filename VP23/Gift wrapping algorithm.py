from tkinter import * # Import tkinter
import math
#import gift_wrapping

def add(event):
    points.append([event.x, event.y])
    repaint()

def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
    repaint()

def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5

# Function that takes three points as tuples and checks if a left turn
# has been made from point p1 to p3, when it goes through p2.
def isLeftTurn(p1, p2, p3):
    return ((p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])) > 0

# Takes a list of points and returns the convex hull of those
# points. 
def getConvexHull(points):
    n = len(points)
    if n < 3:   # need atleast three points
        return []

    # First need to find the leftmost point
    leftmost = points[0]
    for i in range(1, n):
        if points[i][0] < leftmost[0]:
            leftmost = points[i]
            
    # The leftmost point is always on the hull
    hull = [leftmost] 
    endpoint = None
    while endpoint != leftmost:
        endpoint = points[0]
        for i in range(1, n):
            if endpoint == hull[-1] or isLeftTurn(hull[-1], endpoint, points[i]):
                endpoint = points[i]
        hull.append(endpoint)

    return [(x, y) for (x, y) in hull]


def repaint():
    canvas.delete("point")
    if len(points) > 0:
        #
        #
        #
        
        H = getConvexHull(points) # call GiftWrapping getConvexHull
        #
        #
        #
        # Added a check to see if the H was empty or not
        # I got an error that the tuple was empty if this wasn't included
        if H:
            canvas.create_polygon(H, fill = "gray", tags = "point")

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags = "point")
    
def displayInstructions():
    instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20, text = instructions[0], justify = CENTER)
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text = instructions[i], justify = RIGHT)
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text = instructions[i + 1], justify = RIGHT)
        

window = Tk() # Create a window
window.title("Convex Hull") # Set title

width = 500
height = 150
radius = 2
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing points
points = []

displayInstructions()

canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)


window.mainloop() # Create an event loop
