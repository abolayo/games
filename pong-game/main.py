from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Setup
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

# Creating paddles from class Paddle and ball from class Ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard_l = Scoreboard((150, 260))
scoreboard_r = Scoreboard((-150, 260))
# Screen listening to the keyboard to move the paddles
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Game on
game_is_on = True
while game_is_on:
    time.sleep(0.15)  # Slow down the turtle update rate/cycle
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:  # Ball collides with top and lower walls
        ball.bounce_y()

        # Paddle hits the ball, the scoreboard is updated
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        scoreboard_r.update()
        ball.bounce_x()
    if ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        scoreboard_l.update()
        ball.bounce_x()
    # When the player right misses the ball, the ball should start from the origin
    if ball.xcor() > 380:
        scoreboard_l.update()
        ball.reset_direction()

    # when the left player misses the ball
    if ball.xcor() < -380:
        scoreboard_l.update()
        ball.reset_direction()


screen.exitonclick()
