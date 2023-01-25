from turtle import Turtle
SCORE_POSITION = (0,268)
FONT = ("Courier", 20, 'bold')
ALIGNMENT = "Center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(SCORE_POSITION)
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.color("Red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.goto(0,-30)
    #     self.color("white")
    #     self.write(f"Final Score: {self.score}", align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT,  font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{(self.high_score)}")
        self.score = 0
        self.update_score()






