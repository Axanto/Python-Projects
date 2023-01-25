
#Turtle only works with .gif format

from turtle import Turtle, Screen
import pandas
import turtle as tt

bg_img = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
bg_img.shape(image)

guessed_states = []
missing_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Sates Correct", prompt="What's another state's name").title()

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()
    missing_states = all_states

    if answer_state == "Exit":
        for state in guessed_states:
            missing_states.remove(state)
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        break

    if answer_state in all_states:
        t = Turtle()
        t.hideturtle()
        t.penup()
        coors = data[data.state == answer_state]
        t.goto(int(coors.x), int(coors.y)) # when the goto() function is used, data must be integer
        t.write(answer_state)
        # t.write(coors.state.item()) # return the first element of underlying data
        guessed_states.append(answer_state)
        print(guessed_states)


states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("states_to_learn.csv")

