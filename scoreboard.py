import turtle
STATES_LEFT = 50
class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.states_left = STATES_LEFT
        self.states_guessed = 0


    def update_score(self):
        self.states_guessed += 1
