import random
import turtle
from turtle import Turtle, Screen
random.seed()
import heroes
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
"""
x = 360
y = 3
while y != 11:
    for _ in range(y):
        timmy.forward(50)
        timmy.right(x/y)
    y += 1
"""
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        current_heading = timmy.heading()
        timmy.circle(100)
        timmy.setheading(current_heading + 10)


turtle.colormode(255)
timmy.speed(100)
timmy.width(2)
list = [0,90, 180, 270]
i=0
draw_spirograph(5)



screen = turtle.Screen()
screen.exitonclick()


