import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0.05)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")


counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if counter % 6 == 0:
        car_manager.create_car()

    car_manager.car_move()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish_the_level() == True:
        scoreboard.level_up()
        player.start_pos()
        car_manager.increase_speed()









    counter += 1





screen.exitonclick()