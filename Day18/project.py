import random
import turtle
from turtle import Turtle, Screen
import colorgram
"""
rgb_colors = []
colors = colorgram.extract('pic.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""
colors_pic = [(236, 235, 234), (123, 170, 203), (207, 224, 238), (216, 162, 85), (153, 18, 48), (227, 202, 104), (183, 169, 42), (243, 228, 235),
              (204, 130, 169), (188, 72, 36), (60, 99, 151), (230, 239, 232), (192, 86, 125), (31, 32, 75), (75, 156, 96), (119, 186, 161), (159, 63, 105),
              (66, 20, 34), (67, 32, 27), (68, 132, 70), (231, 169, 193), (214, 87, 60),
              (35, 49, 121), (146, 209, 227), (105, 114, 173), (149, 28, 22), (75, 151, 158), (157, 191, 229), (26, 87, 59), (237, 170, 165)]

timmy = Turtle()
turtle.colormode(255)
timmy.speed(500)

timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for i in range (1, number_of_dots + 1):
    timmy.dot(20, random.choice(colors_pic))
    timmy.forward(50)

    if i % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
