from turtle import Turtle, Screen
import time
from random import randint, choice

screen = Screen()
timmy=Turtle()
timmy.speed(4)
# timmy.pensize(20)
timmy.shape("classic")


# timmy.color("DarkSeaGreen3")
# time.sleep(0.5)
# timmy.lt(90)
# timmy.backward(250)
# timmy.rt(90)
# timmy.pen(pencolor="green", fillcolor="DarkSeaGreen3", pensize=20, speed=2)
# timmy.begin_fill()
# timmy.circle(250)
# timmy.end_fill()
# timmy.lt(90)
# timmy.backward(100)
# time.sleep(1)
# timmy.reset()


# timmy.fd(100)
# for i in range(3):
#     time.sleep(0.25)
#     timmy.rt(90)
#     timmy.fd(100)

# for _ in range(10):
#     timmy.forward(10)
#     time.sleep(0.25)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# screen.colormode(255)
# timmy.pensize(5)
# time.sleep(0.5)
# for i in range(3,11):
#     r=randint(0,255)
#     g=randint(0,255)
#     b=randint(0,255)
#     timmy.pencolor((r,g,b))
#     for j in range(i):
#         timmy.rt(360/i)
#         timmy.fd(150)


# timmy.pensize(15)
# def checkActivity(act):  #setHeading
#     if act == "fd":
#         timmy.fd(60)
#     elif act == "bk":
#         timmy.bk(60)
#     elif act == "rtf":
#         timmy.rt(90)
#         timmy.fd(60)
#     elif act == "rtb":
#         timmy.rt(90)
#         timmy.bk(60)
#     elif act == "ltf":
#         timmy.lt(90)
#         timmy.fd(60)
#     else:
#         timmy.lt(90)
#         timmy.bk(60)
# screen.colormode(255)
# i=0
# activities=["fd","bk","rtf","rtb","ltf","ltb"]
# while i!=100:
#     r=randint(0,255)
#     g=randint(0,255)
#     b=randint(0,255)
#     timmy.pencolor((r,g,b))
#     randomAct=choice(activities)
#     checkActivity(randomAct)
#     i+=1


# screen.colormode(255)
# timmy.pensize(2)
# for i in range(36):
#     r=randint(0,255)
#     g=randint(0,255)
#     b=randint(0,255)
#     timmy.pencolor((r,g,b))
#     timmy.circle(100)
#     timmy.lt(10)


screen.exitonclick()