import colorgram
import turtle as t

tu=t.Turtle()
screen=t.Screen()
tu.speed(15)
tu.hideturtle()
tu.color("white")
rgb_colors=[(201, 166, 110), (238, 241, 246),  (146, 75, 51), (222, 202, 138), (167, 151, 46), 
(246, 243, 238), (55, 93, 123), (161, 143, 157), (133, 163, 183), (49, 117, 87), (197, 92, 73), 
(134, 33, 22), (68, 45, 38), (17, 95, 74), (148, 178, 148), (105, 74, 77), (232, 176, 165), (57, 46, 49), 
(40, 59, 71), (184, 205, 174), (136, 26, 29), (240, 246, 242), (83, 147, 126), (25, 82, 90), 
(175, 97, 100), (19, 70, 59), (247, 242, 244), (48, 65, 81), (67, 63, 58), (111, 125, 149), 
(220, 175, 181), (173, 199, 206), (184, 190, 206), (110, 134, 140)]


# colors = colorgram.extract("img.jpg",84)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     rgb_colors.append((r,g,b))


tu.goto(-225,-225)
screen.colormode(255)
y=-225
color=0
for col in range(10):
    tu.pendown()
    for dot in range (10):
        tu.color(rgb_colors[color])
        tu.pencolor(rgb_colors[color])
        tu.dot(20)
        tu.penup()
        tu.forward(50)
        tu.pendown()
        if color<len(rgb_colors)-1:
            color+=1
        else:
            color=0
    tu.penup()
    y=y+50
    tu.goto(-225,y)

screen.exitonclick()