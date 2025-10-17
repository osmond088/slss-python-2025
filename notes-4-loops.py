# Drawing and Loops
# Osmond Fu
# 14 October 2025

from optparse import make_option
import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")

# TMNT - turtles
# create a turtle called mike
mike = turtle.Turtle()
mike.turtlesize(5)  # set size
# mike.shape("turtle") # shape
mike.color("orange")  # colour

# move mike around
mike.speed(4)
mike.width(4)

# # Snowman
# mike.color("lightblue")
# mike.begin_fill()
# # Small circle
# mike.circle(100)
# mike.end_fill()
# mike.penup()
# mike.goto(0, 200)
# mike.begin_fill()
# # Medium Circle
# mike.circle(80)
# mike.end_fill()
# mike.goto(0, 360)
# mike.begin_fill()
# # Smallest circle
# mike.circle(50)
# mike.end_fill()
# mike.goto(-25, 420)
# mike.shapesize(1)
# mike.color("black")
# mike.shape("circle")
# # Face
# mike.stamp()
# mike.goto(25, 420)
# mike.stamp()
# mike.goto(0, 400)
# mike.stamp()
# # Buttons
# mike.goto(0, 340)
# mike.stamp()
# mike.goto(0, 300)
# mike.stamp()
# mike.goto(0, 260)
# mike.stamp()


# Create a function to make cookies
def make_cookies(x: int, y: int):
    # Cookie Making
    # Set the colour of our choco chip cookie
    mike.color("brown")
    # Draw a circle to represent our cookie
    mike.shapesize(1)
    mike.pu()
    mike.setheading(0)  # mike points east
    mike.goto(-5 + x, -30 + y)
    mike.pd()
    mike.circle(30)
    # Put a chocolate chip at the top-right
    mike.pu()
    mike.goto(10 + x, 10 + y)
    mike.stamp()
    # Put a chocolate chip at the bottom-right
    mike.goto(10 + x, -10 + y)
    mike.stamp()
    # Put a choco chip at the bottom-left
    mike.goto(-10 + x, -10 + y)
    mike.stamp()
    # Choco chip at the top-left
    mike.goto(-10 + x, 10 + y)
    mike.stamp()
    # Chocolate chip in the middle
    mike.goto(0 + x, 0 + y)
    mike.stamp()


# make_cookies(0, 0)     # origin
# make_cookies(100, 100) # (100,100)
# make_cookies(-100, -100)
# make_cookies(-100, 100)
# make_cookies(100, -100)

# Make cookies in an x
for counter in range(50):
    counter = counter * 50
    make_cookies(-counter, -counter)
    make_cookies(counter, -counter)
    make_cookies(counter, counter)
    make_cookies(-counter, counter)

window.exitonclick()
