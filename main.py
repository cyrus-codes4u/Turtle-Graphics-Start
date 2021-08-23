from turtle import Turtle, Screen

turtle = Turtle()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for j in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


for i in range(3, 11):
    draw_shape(i)


screen = Screen()
screen.exitonclick()
