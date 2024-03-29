import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(scoreboard.reset_game, "e")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.update()
        snake.extended()
        food.refresh()

    if snake.head.xcor() > 385 or snake.head.xcor() < -385 or snake.head.ycor() > 385 or snake.head.ycor() < -385:
        snake.reset()
        scoreboard.reset()

    # Head hit the body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
