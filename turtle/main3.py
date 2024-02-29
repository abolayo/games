import turtle as t
import random
screen = t.Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title='Turtle game', prompt='Choose a turtle, enter it color: ')
colors = ['red', 'green', 'blue', 'black', 'purple', 'yellow']
y_cood = [-70, -30, 10, 50, 90, 130]
all_turtles = []
game_on = False

if user_choice:
    game_on = True


for turtle_index in range(6):
    turtle = t.Turtle(shape='turtle')
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230, y=y_cood[turtle_index])
    all_turtles.append(turtle)
while game_on:
    for i in all_turtles:
        i.forward(random.randint(0, 10))
        if i.xcor() > 220:
            game_on = False
            screen.clear()
            winning_color = i.pencolor()
            if user_choice == i.color():
                print(f"you won!, the winning turtle is {winning_color} ")
            else:
                print(f"you lost!, the winning turtle is {winning_color} ")







screen.exitonclick()
