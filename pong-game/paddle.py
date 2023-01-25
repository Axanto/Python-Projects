from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self,position):
        self.shape("square")
        self.color("#A5C9CA")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def move_up(self):
        if self.ycor() < 300:
            new_y = self.ycor() + 25
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -300:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)
