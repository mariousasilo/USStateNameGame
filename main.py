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
guessed_states = []
correct_answer = len(guessed_states)


while correct_answer < num_states:
    player = screen.textinput(f"{correct_answer}/{num_states} States Correct", "What's another state name?").title()
    if player in states and player not in guessed_states:
        guessed_states.append(player)
        state_details = data[data["state"] == player]
        x = int(state_details["x"])
        y = int(state_details["y"])
        StateName(state_name=player, x_axis=x, y_axis=y)
        correct_answer = len(guessed_states)
    elif player == "Exit":
        missed_states = [state for state in states if state not in guessed_states]
        df_missed = pandas.DataFrame(data=missed_states)
        df_missed.to_csv("missed_states.csv")
        df_guessed = pandas.DataFrame(data=guessed_states)
        df_guessed.to_csv("guessed_states.csv")
        break


