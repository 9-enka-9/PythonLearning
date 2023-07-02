import turtle as t
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scr=t.Screen()
scr.setup(width=800,height=600)
scr.bgcolor("black")
scr.title("Pong Game")
scr.tracer(0)

rightPaddle=Paddle((350,0))
leftPaddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

scr.listen()
scr.onkeypress(rightPaddle.goUp,"Up")
scr.onkeypress(rightPaddle.goDown,"Down")

scr.onkeypress(leftPaddle.goUp, "w")
scr.onkeypress(leftPaddle.goDown, "s")

isGameOn = True
while isGameOn:
	scr.update()
	ball.move()
	time.sleep(ball.moveSpeed)
	
	# Detect collision with wall
	if ball.ycor()>=290 or ball.ycor()<=-290:
		ball.bounceWall() # IMPORTANT KNOWLEDGE
		
	# Detect collision with paddles
	if (ball.distance(rightPaddle) < 50 and ball.xcor() > 320) or (ball.distance(leftPaddle) < 50 and ball.xcor() < -320):
		ball.bouncePaddle()
		
	# Detect when paddle misses
	if ball.xcor()>450:
		time.sleep(1)
		scoreboard.leftScore+=1
		scoreboard.update()
		ball.refresh()

	if ball.xcor()<-450:
		time.sleep(1)
		scoreboard.rightScore+=1
		scoreboard.update()
		ball.refresh()
	
	












scr.exitonclick()