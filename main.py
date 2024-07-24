import turtle
from turtle import Turtle, Screen

import pandas

scr = Screen()
scr.title("U.S. States Game")
image = "blank_states_img.gif"
scr.addshape(image)
turtle.shape(image)

naming = Turtle()

data = pandas.read_csv("50_states.csv")
states = data["state"]  # extracted a series of state
list_of_states = states.to_list()  # series.method() = states here is series, to_list() is a method
# print(list_of_states)
score = 0
guessed_states = []

def positioning_states():
    global score
    for state in list_of_states:

        if state == input_state:
            guessed_states.append(state)
            answer_row = data[data["state"] == state]
            naming.penup()
            naming.hideturtle()
            x = int(answer_row["x"])
            y = int(answer_row["y"])
            naming.goto(x=x, y=y)
            naming.write(arg=input_state, align="center", font=("Arial", 8, "normal"))
            score += 1


while len(guessed_states) < 50:
    answer = scr.textinput(title=f"{score}/50 Guess the State", prompt="Write another state's name:")
    input_state = answer.title()
    if input_state == "Exit":
        # list comprehension
        missing_states = [state for state in list_of_states if state not in guessed_states]
        # missing_states = []
        # for state in list_of_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to learn.csv")
        break

    positioning_states()
