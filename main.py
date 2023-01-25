#import colorgram

# colors = colorgram.extract("image.png", 30)

# color_list = []
# for i in colors:
#     rgb = i.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     temp_tuple = (r,g,b)
#     color_list.append(temp_tuple)
#
# print(color_list)

color_list = [(231, 233, 237), (235, 231, 233), (225, 233, 227), (207, 160, 82), (54, 89, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (133, 177, 203), (157, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 169), (85, 121, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (46, 74, 77), (161, 202, 219), (80, 74, 44), (56, 126, 122), (218, 176, 188), (170, 206, 171), (220, 182, 168)]

import turtle
from turtle import Turtle, Screen
import random


dotty = Turtle()
turtle.colormode(255)
x_cor = -225
y_cor = -225
dotty.speed("fastest")
dotty.hideturtle()
for i in range(9):
    dotty.penup()
    dotty.setposition(x_cor, y_cor)
    dotty.dot(20,random.choice(color_list))
    for x in range(9):
        dotty.forward(50)
        dotty.dot(20,random.choice(color_list))
    y_cor += 50

screen = Screen()
screen.exitonclick()