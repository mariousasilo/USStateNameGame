from turtle import Turtle


FONT = ('Arial', 8, 'normal')


class StateName(Turtle):

    def __init__(self, state_name, x_axis, y_axis):
        super().__init__()
        self.turtle_state_config()
        self.goto(x=x_axis, y=y_axis)
        self.write(arg=state_name, align="center", font=FONT)

    def turtle_state_config(self):
        self.penup()
        self.hideturtle()
