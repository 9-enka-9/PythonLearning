import turtle as t
from paddle import Paddle

scr=t.Screen()
scr.setup(width=800,height=600)
scr.bgcolor("black")
scr.title("Pong Game")
scr.tracer(0)

rightPaddle=Paddle(350,0)
leftPaddle=Paddle(-350,0)

scr.listen()
scr.onkeypress(rightPaddle.goUp,"Up")
scr.onkeypress(rightPaddle.goDown,"Down")

scr.onkeypress(leftPaddle.goUp, "w")
scr.onkeypress(leftPaddle.goDown, "s")

isGameOn = True
while isGameOn:
	scr.update()













scr.exitonclick()