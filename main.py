from turtle import Screen
from statename_turtle import StateName
import pandas

screen = Screen()
screen.title("Name the US-State Game")
screen.bgpic(picname="blank_states_img.gif")
screen.setup(width=725, height=491)

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
num_states = len(states)

correct_answer = 0
while correct_answer < num_states:
    player = screen.textinput(f"{correct_answer}/{num_states} States Correct", "What's another state name?").title()
    if player in states:
        correct_answer += 1
        state_details = data[data["state"] == player]
        x = int(state_details["x"])
        y = int(state_details["y"])
        StateName(state_name=player, x_axis=x, y_axis=y)

screen.exitonclick()
