import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
states = pd.read_csv("50_states.csv")
all_states = states["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_data = states[states.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)

        # Update the screen

# turtle.mainloop()
# screen.exitonclick()
