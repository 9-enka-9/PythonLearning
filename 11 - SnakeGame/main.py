import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scr=t.Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0) # to make squares move without space
scr.listen()
snake=Snake()
food = Food()
scoreboard=Scoreboard()

scr.onkey(fun=snake.up, key="Up")
scr.onkey(fun=snake.down, key="Down")
scr.onkey(fun=snake.left, key="Left")
scr.onkey(fun=snake.right, key="Right")

isGameOn=True
while isGameOn:
    scr.update() # show the move of squares, use with tracer method above
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.snake[0].distance(food) <= 15:
        food.refresh()
        scoreboard.updateScore()
        snake.createSegment()
    
    # Detect collision with wall
    if snake.snake[0].xcor()>295 or snake.snake[0].xcor()<-295 or snake.snake[0].ycor()>295 or snake.snake[0].ycor()<-295:
        isGameOn=False
        scoreboard.gameOver()
    
    # Detect collision with tail
    for segment in snake.snake[1:-1]:
        if snake.snake[0].distance(segment)<10:
            isGameOn=False 
            scoreboard.gameOver()
            
        






scr.exitonclick()