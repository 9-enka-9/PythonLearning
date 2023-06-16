import turtle as t
from random import randint

isRaceOn=False
scr=t.Screen()
scr.setup(width=500,height=400)
guess=scr.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

colors=["purple", "blue","green","yellow","orange","red"]
tortoises=[]
y=110
for color in colors:
    tur=t.Turtle(shape="turtle")
    tur.color(color)
    tur.penup()
    tur.goto(x=-220,y=y)
    y-=40
    tortoises.append(tur)
    
if guess:
    isRaceOn=True
    
while isRaceOn:
    for turtle in tortoises:
        distance=randint(1,10)
        turtle.forward(distance)
        if turtle.xcor() >= 219:
            isRaceOn=False
            winningColor=turtle.pencolor()
            if winningColor==guess:
                print(f"You've won! The {winningColor} turtle is the winner.")
            else:
                print(f"You've lost! The {winningColor} turtle is the winner.")
            break
        
    
    
scr.exitonclick()
