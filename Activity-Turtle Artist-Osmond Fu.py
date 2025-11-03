# Turtle Artist
# Author: Osmond Fu
# 28 October

import turtle

# A one-of-a-kind drawing

wn = turtle.Screen()
wn.bgcolor("lightblue")
t = turtle.Turtle()
t.speed(0)


# draw grass at bottom
def draw_grass():
    t.penup()
    t.goto(-400, -200)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.forward(800)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(800)
    t.left(90)
    t.forward(100)
    t.end_fill()


# this draws the sun
def draw_sun():
    t.penup()
    t.goto(200, 150)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()


# draws a tree recursively
# length = how long the branch is
# depth = how many times to split the branches
def draw_tree(length, depth):
    # base case - stop when depth is 0
    if depth == 0:
        return

    # draw the branch
    t.forward(length)

    # save where we are
    pos = t.pos()
    heading = t.heading()

    # go right and draw smaller branch
    t.right(30)
    draw_tree(length * 0.7, depth - 1)

    # go back to where we were
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

    # go left and draw smaller branch
    t.left(25)
    draw_tree(length * 0.7, depth - 1)

    # return to original position
    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()


draw_grass()
draw_sun()

# first tree
t.penup()
t.goto(-150, -100)
t.setheading(90)
t.pendown()
t.color("brown")
t.pensize(3)
draw_tree(60, 7)


# draw a house
def draw_house():
    # draw the main part of house
    t.penup()
    t.goto(50, -100)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.setheading(0)
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

    # draw the roof
    t.goto(50, 0)
    t.color("brown")
    t.begin_fill()
    t.goto(100, 50)
    t.goto(150, 0)
    t.goto(50, 0)
    t.end_fill()

    # draw door
    t.goto(80, -100)
    t.color("blue")
    t.begin_fill()
    t.setheading(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.end_fill()


draw_house()

t.hideturtle()

wn.mainloop()
