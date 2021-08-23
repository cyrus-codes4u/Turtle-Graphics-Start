from turtle import Turtle, Screen

turtle = Turtle()

for i in range(10):
    turtle.forward(10)
    if turtle.isdown():
        turtle.up()
    else:
        turtle.down()

screen = Screen()
screen.exitonclick()
