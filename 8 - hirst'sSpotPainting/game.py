import turtle

screen=turtle.Screen()
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)

# player_one.goto(300,60)
# player_one.pendown()
# player_one.circle(40)
# player_one.penup()
# player_one.goto(-200,100)
# player_two.goto(300,-140)
# player_two.pendown()
# player_two.circle(40)
# player_two.penup()
# player_two.goto(-200,-100)

screen.exitonclick()