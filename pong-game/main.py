from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("#2C3333")
screen.title("Pong Game")
screen.tracer(0)

dash = Turtle()
dash.color("#FEC260")
dash.pensize(5)
dash.penup()
dash.goto(0,370)
dash.seth(270)
dash.hideturtle()
for i in range(10):
    dash.penup()
    dash.forward(35)
    dash.pendown()
    dash.forward(35)
    dash.pendown()


paddle_l = Paddle((-470, 0))
paddle_r = Paddle((470, 0))
ball = Ball()
scoreboard_r = Scoreboard((50,270))
scoreboard_l = Scoreboard((-50, 270))

screen.listen()
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")
screen.onkey(ball.pause_game, "p")
screen.onkey(ball.continue_game, "c")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_move()

    if abs(ball.ycor()) > 330:
        ball.ball_bounce_wall()

    if ball.distance(paddle_r) < 63 or ball.distance(paddle_l) < 63 and abs(ball.xcor()) > 450:
        if abs(ball.xcor()) > 480:
            pass
        else:
            ball.ball_bounce_paddle()

    if ball.xcor() > 480:
        scoreboard_l.increase_score()
        ball.reset_position()

    if ball.xcor() < -480:
        scoreboard_r.increase_score()
        ball.reset_position()


screen.exitonclick()

# SOMETIMES THE BALL GET STUCKED BETWEEN TWO PADDLE. I WILL FIX THAT ONE DAY.