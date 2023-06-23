import turtle as t
import time
from snake import Snake

scr=t.Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0) # to make squares move without space
scr.listen()
snake=Snake()

scr.onkey(fun=snake.up, key="Up")
scr.onkey(fun=snake.down, key="Down")
scr.onkey(fun=snake.left, key="Left")
scr.onkey(fun=snake.right, key="Right")

isGameOn=True
while isGameOn:
    scr.update() # show the move of squares, use with tracer method above
    time.sleep(0.1)
    snake.move()
    
    
        
        






scr.exitonclick()