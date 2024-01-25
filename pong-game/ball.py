from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.y_move = 10
        self.x_move = 10

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_direction(self):
        self.goto(0, 0)
        self.bounce_x()

