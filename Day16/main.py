from turtle import Turtle, Screen
import module

# print(module.variable)
# arturo = Turtle()
# print(arturo)
# arturo.shape("turtle")
# arturo.color("blue")
# arturo.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
