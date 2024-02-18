import turtle
from turtle import Turtle
import random

directions = [0, 90, 180, 270]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_cl = (r, g, b)

    return random_cl


tom = Turtle()
tom.pensize(10)  # controlling the pen size of the turtle
tom.speed('fastest')  # controlling the speed of the turtle
tom.hideturtle()  # hiding the turtle

for _ in range(500):
    tom.color(random_color())
    tom.forward(50)
    tom.setheading(random.choice(directions))

turtle.mainloop()
