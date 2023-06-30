import turtle as t
from paddle import Paddle
from ball import Ball
import time

scr=t.Screen()
scr.setup(width=800,height=600)
scr.bgcolor("black")
scr.title("Pong Game")
scr.tracer(0)

rightPaddle=Paddle((350,0))
leftPaddle=Paddle((-350,0))
ball=Ball()

scr.listen()
scr.onkeypress(rightPaddle.goUp,"Up")
scr.onkeypress(rightPaddle.goDown,"Down")

scr.onkeypress(leftPaddle.goUp, "w")
scr.onkeypress(leftPaddle.goDown, "s")

isGameOn = True
while isGameOn:
	scr.update()
	ball.move()
	time.sleep(0.003)
	
	# Detect collision with wall
	if ball.ycor()>=290 or ball.ycor()<=-290:
		ball.bounce() # IMPORTANT KNOWLEDGE













scr.exitonclick()