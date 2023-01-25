from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#E7F6F2")
        self.penup()
        self.setheading(random.randint(0,360))
        self.move_speed = 0.06
        self.temp = 0

    def ball_move(self):
        self.fd(15)

    def ball_bounce_wall(self):
        new_heading = -self.heading()
        self.setheading(new_heading)
        self.fd(3)

    def ball_bounce_paddle(self):
        new_heading = 180 - self.heading()
        self.setheading(new_heading)
        self.fd(3)
        self.move_speed *= 0.85


    def reset_position(self):
        self.home()
        self.move_speed = 0.08

    def pause_game(self):
        self.temp = self.move_speed
        self.move_speed = 2

        self.write("I'm unstoppable!!", align="right", font = ("Arial", 15 , 'bold'))

    def continue_game(self):
        self.clear()
        self.move_speed =self.temp

