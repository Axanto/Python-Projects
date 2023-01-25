from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#A10035")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randrange(-280, 300, 20)
        random_y = random.randrange(-280, 300, 20) # using 20 pace step better for arrangement because our snake moves by 20p
        self.goto(random_x, random_y)
