# from turtle import Screen, Turtle
# timmy=Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.backward(200)

# myScreen=Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

from prettytable import PrettyTable
from os import system,name

_=system('cls')

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align='l'

print(table)


