#!/bin/python3

import turtle
import random

shelly = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colors = ["blue", "cyan", "purple", "pink", "violet", "black"]
shelly.color("cyan")


def branch():
    l= 0
    while l < 3:
        shelly.color(random.choice(colors))
        l = l+1
        for j in range(3):
            shelly.forward(30)
            shelly.backward(30)
            shelly.right(45)
        shelly.left(90)
        shelly.backward(30)
        shelly.left(45)
    shelly.right(90)
    shelly.forward(90)

k = 0
while k  < 8:
    branch()
    shelly.left(45)
    k = k+1
