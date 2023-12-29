import random
import turtle as t

tim = t.Turtle()
my_shape = tim.shape('turtle')

colour = ['red', 'blue', 'green', 'black', 'yellow']
directions = [0, 90, 180, 270]
tim.speed('fastest')
t.colormode(255)
for i in range(20):
    tim.pensize(2)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colour))
    tim.forward(25)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
