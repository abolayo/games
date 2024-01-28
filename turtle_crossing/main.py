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
# Screen listening to Up key
screen.listen()
screen.onkey(player.move_forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for i in car.all_cars:
        if player.distance(i) < 10:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        scoreboard.update()
        car.level_up()
        player.goto_start()


screen.exitonclick()
