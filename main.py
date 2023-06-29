import turtle as trtl
import random

# The purpose of this program is to draw a unique image depending on the user input


#definitions of how to draw the shapes
def circle():
    trtl.circle(30)


def triangle():
    trtl.circle(30, 360, 3)


def square():
    trtl.circle(30, 360, 4)


def pentagon():
    trtl.circle(30, 360, 5)


def hexagon():
    trtl.circle(30, 360, 6)


def octagon():
    trtl.circle(30, 360, 8)


#list of colors
colors = [
    "blue", "brown", "gray", "green", "indigo", "purple", "violet", "cyan",
    "gold", "orange", "pink", "red", "white", "yellow"
]
#list of pensizes
pensizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

images = 0
while (images < 1):  #only one image should be on display at a time to aviod too much overlap and messiness, but if the user wishes, they can enter another shape to draw on top of their previous shape to add more artistic design 
    shape = input(
        "Enter a shape to draw: "
    )  #asks the user to enter a shape to draw that makes up the image
    if shape == "circle":  #draws a image of circles
        for color in colors:
            trtl.color(random.choice(colors))
            trtl.pensize(random.choice(pensizes))
            trtl.left(26)
            circle()

    elif shape == "triangle":  #draws a image of traingles
        for color in colors:
            trtl.color(random.choice(colors))
            trtl.pensize(random.choice(pensizes))
            trtl.left(26)
            triangle()

    elif shape == "square":  #draws a image of sqaures
        for color in colors:
            trtl.color(random.choice(colors))
            trtl.pensize(random.choice(pensizes))
            trtl.left(26)
            square()

    elif shape == "pentagon":  #draws a image of pentagons
        for color in colors:
            trtl.color(random.choice(colors))
            trtl.pensize(random.choice(pensizes))
            trtl.left(26)
            pentagon()

    elif shape == "hexagon":  #draws a image of hexagons
        for color in colors:
            trtl.color(random.choice(colors))
            trtl.pensize(random.choice(pensizes))
            trtl.left(26)
            hexagon()

    elif shape == "octagon":  #draws a image of octogons
        for color in colors:
            trtl.color(random.choice(colors))
            trtl.pensize(random.choice(pensizes))
            trtl.left(26)
            octagon()

    else:
        print("That is not an available shape, please enter another shape")
