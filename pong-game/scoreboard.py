from turtle import Turtle

FONT = ("Courier", 50, 'bold')
ALIGNMENT = "Center"

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.update_score(position)


    def update_score(self,position):
        self.penup()
        self.color("#80558C")
        self.goto(position)
        self.hideturtle()
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"{self.score}", align=ALIGNMENT, font=FONT)





