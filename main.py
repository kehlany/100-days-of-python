import random
import turtle
color_list = [(252, 251, 249), (253, 244, 250), (246, 254, 251), (242, 248, 251), (185, 177, 5), (178, 3, 66),
              (246, 69, 3), (6, 141, 28), (245, 20, 150), (40, 195, 238), (192, 4, 1), (5, 131, 208)]
from turtle import Turtle, Screen
tim = Turtle()
dot_size = 20
spacing = 50
rows = 10
column = 10
start_x = -200
start_y = -200
turtle.colormode(255)
tim.penup()
tim.goto(x = -200, y = -200)
for row in range (rows):
    for col in range(column):
        tim.dot(20)
        tim.forward(spacing)
        tim.color(random.choice(color_list))
    start_y += spacing
    tim.goto(start_x, start_y)



screen = Screen()
screen.exitonclick()