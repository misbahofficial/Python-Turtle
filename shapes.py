from turtle import Turtle, Screen
import random

tom = Turtle() # creating turtle object


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tom.forward(100)
        tom.right(angle)


for side in range(3, 11):
    colors = ['blue', 'saddle brown', 'brown', 'magenta', 'lime', 'orange', 'cyan']
    tom.color(random.choice(colors))
    draw_shape(side)

# codes for not exiting instantly
screen = Screen()
screen.exitonclick()
