import turtle as t
import time
from snake import Snake

scr=t.Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

snake=Snake()

isGameOn=True
while isGameOn:
    scr.update()
    time.sleep(0.2)
    snake.move()
    
    
        
        






scr.exitonclick()