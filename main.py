import turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()
data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()
# print(data[data["state"] == "Utah"]["x"])
game_on = True
states_guess = []
answers=[]

def handle_guess(guess):
    if guess in states_list and guess not in states_guess:
        state_data = data[data.state == guess]
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        print(state_data.iloc[0].x)
        state.goto(int(state_data.iloc[0].x),int(state_data.iloc[0].y))
        state.write(user_input)
        states_guess.append(user_input)
        scoreboard.update_score()

while game_on:
    user_input = screen.textinput(title=f"{scoreboard.states_guessed}/{scoreboard.states_left} States Correct", prompt="Whats a states name?").title()
    if user_input == "Exit":
        break
    handle_guess(user_input)
    if scoreboard.states_guessed == 50:
        game_on = False
        screen.textinput("You Won!!!!")


for state in states_list:
    if state not in states_guess:
        answers.append(state)

ds = pandas.DataFrame(answers)
ds.to_csv("StatesToLearn.csv")