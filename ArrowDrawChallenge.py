# ArrowDrawChallenge.py Creates a program to draw using the arrow keys.
# Billy Ridgeway
# Lets the user draw on the screen and increase and decrease the thickness
# of the pen.

import turtle                   # Imports the turtle library.
t = turtle.Pen()                # Creates a pen named t.
t.speed(0)                      # Sets the pen's speed to fast.
t.turtlesize(2,2,2)             # Sets the size of the pen.
turtle.bgcolor("blue")          # Sets the background color to blue.
t.pencolor("yellow")            # Sets the pen's color to yellow.

def up():                       # Defines the function for moving the pen forward 50 pixels.
    t.forward(50)
def left():                     # Defines the function for turning the pen to the left by 15 degrees.
    t.left(15)
def right():                    # Defines the function for turning the pen to the right by 15 degrees.
    t.right(15)
def move(x,y):                  # Defines the function that will move the pen to the x y coordinates where the screen has been clicked.
    t.penup()                   # Stops the pen from drawing while moving to the new position.
    t.setpos(x,y)               # Sets the pen to the new x y position.
    t.pendown()                 # Set the pen to draw.
def thicker():                  # Defines the function to increase the thickness of the pen.
    t.width( t.width() + 2 )    # Increases the pen's width by 2 when called.
def thinner():                  # Defines the function to decrease the thickness of the pen.
    t.width( t.width() - 2 )    # Decreases the pen's width by 2 when called.
    
turtle.onkeypress(up, "Up")         # Calls the up function when the up arrow key is pressed.
turtle.onkeypress(left, "Left")     # Calls the left function when the left arrow key is pressed.
turtle.onkeypress(right, "Right")   # Calls the right function when the right arrow key is pressed.
turtle.onkeypress(thicker, ">")     # Calls the thicker function when the greater than key is pressed.
turtle.onkeypress(thinner, "<")     # Calls the thinner function when the less than key is pressed.
turtle.listen()                     # Listens for keyboard events.
turtle.onscreenclick(move)          # Calls the move function to reassign the x y coordinates of the pen to the location the user clicked.
