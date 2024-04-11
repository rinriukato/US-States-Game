import turtle
import pandas

IMG = "blank_states_img.gif"
STATES = "50_states.csv"
FONT = ("Arial", 7, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMG)
turtle.shape(IMG)

states = pandas.read_csv(filepath_or_buffer=STATES)
states_correct = 0
guessed_states = []

while states_correct != 50:
    answer_state = screen.textinput(title=f"{states_correct}/50 Guess the State", prompt="Name a state!").title()

    if answer_state == "Exit":
        break

    if answer_state.title() in states['state'].tolist():
        this_state = states[states["state"] == answer_state]
        guessed_states.append(answer_state)
        x = this_state['x'].tolist()
        y = this_state['y'].tolist()
        turtle_state = turtle.Turtle()
        turtle_state.hideturtle()
        turtle_state.penup()
        turtle_state.setposition(x=x[0], y=y[0])
        turtle_state.write(arg=f"{answer_state}", move=False, align='center', font=FONT)
        states_correct += 1
    else:
        pass


all_states = states["state"].tolist()
missing_states = [state for state in all_states if state not in guessed_states]

state_dict = {
    "Missing States": missing_states
}

new_data = pandas.DataFrame(state_dict)
new_data.to_csv("missing_states.csv")

turtle.mainloop()


