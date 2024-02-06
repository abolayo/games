from turtle import Turtle

FONT = ('Ariel', 20, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.color('white')
            self.penup()
            self.hideturtle()
            # self.goto(screen.title())
            self.write_score()

        def write_score(self):
            self.clear()
            self.write(f'Score: {self.score} , High Score: {self.high_score}', True, align=ALIGNMENT, font=FONT)

        def update(self):
            self.score += 2
            self.write_score()

        def foul(self):
            self.score -= 1
            self.write_score()

