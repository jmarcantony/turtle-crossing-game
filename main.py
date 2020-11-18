import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")
screen.onkey(fun=screen.bye, key="Escape")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    count += 1
    if count % 6 == 0:
        car.create_car()
    if count > 6:
        car.move()

    for cars in car.all_cars:
        if player.distance(cars) < 39:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        time.sleep(0.1)
        car.increase_speed()
        player.level_up()
        scoreboard.update_score()

screen.exitonclick()
