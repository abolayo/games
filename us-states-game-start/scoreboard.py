from turtle import Turtle

FONT = ('Ariel', 20, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        # self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score}', True, align=ALIGNMENT, font=FONT)

    def update(self):
        self.score += 1
        self.write_score()



