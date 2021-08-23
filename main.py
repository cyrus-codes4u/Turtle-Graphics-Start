import turtle as t
import random

ANGLE_CHANGE = 3
t.colormode(255)

turtle = t.Turtle()
turtle.width(3)
turtle.speed("fastest")


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for i in range(int(360/ANGLE_CHANGE)):
    turtle.color(rand_color())
    turtle.circle(100)
    current_direction = turtle.heading()
    turtle.setheading(current_direction+ANGLE_CHANGE)

screen = t.Screen()
screen.exitonclick()
