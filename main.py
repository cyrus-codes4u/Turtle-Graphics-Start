from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.width(5)
turtle.speed("fastest")
colors = ["DarkOrchid", "wheat", "SeaGreen", "SlateGray", "DeepSkyBlue", "IndianRed"]
directions = [0, 90, 180, 270]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for j in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


for i in range(1000):
    turtle.color(random.choice(colors))
    turtle.setheading(random.choice(directions))
    turtle.forward(10)


screen = Screen()
screen.exitonclick()
