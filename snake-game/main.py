from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("#2A0944")
screen.title("Snake Game")
screen.tracer(0)
# it's used for controlling the animations
# In this part, it's not doing any change on the screen until update code is written

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def eat_more():
    for segments in snake.segment:
        while food.distance(segments) < 3:
            food.refresh()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on: # "while loop" is using for the game is on until it's said to be close
    screen.update() # when the update is written, snake is moving with its whole body
    # because screen will be updated after all objects have been moved due to loop below
    time.sleep(0.07)

    snake.move()

    #FOOD SPAWN TEST
    #screen.onkey(key="space", fun=eat_more)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print("NOM")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        for segments in snake.segment:
            if food.pos() == segments.pos():
                food.refresh()
                print(food.pos())
                print(segments.pos())


    # Detect collision with the wall
    # if abs(snake.head.xcor()) > 280:
    #     snake.head.goto(-snake.head.xcor(), snake.head.ycor())
    # if abs(snake.head.ycor()) > 280:
    #     snake.head.goto(snake.head.xcor(), -snake.head.ycor())
    if abs(snake.head.ycor()) > 280 or abs(snake.head.xcor()) > 280:
        # is_game_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with the tail
    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 10:
            # is_game_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()

#Note: It could be better with improvements yet it's playable