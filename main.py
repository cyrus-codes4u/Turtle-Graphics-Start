import turtle as t
import random

t.colormode(255)
turtle = t.Turtle()
turtle.width(15)
turtle.speed("fastest")
directions = [0, 90, 180, 270]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for j in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for i in range(1000):
    turtle.color(rand_color())
    turtle.setheading(random.choice(directions))
    turtle.forward(10)


screen = t.Screen()
screen.exitonclick()
