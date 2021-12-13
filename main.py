from turtle import Turtle, Screen
import pandas

turtle = Turtle()

# screen setup
screen = Screen()
screen.title("US States Game")
screen.screensize(1000,1000)
screen.bgpic("blank_states_img.gif")

# turtle setup
FONT = ("Verdana", 10, "normal")
FONT2 = ("Verdana", 25, "normal")
turtle.hideturtle()
turtle.penup()

# data setup
states_csv = pandas.read_csv("50_states.csv")
states_guessed = []
states_to_learn = []

name = screen.textinput("Name", "Please input your name:")
screen.textinput("America States",
f'''Kia Ora {name}, this game tests your knowledge about American states.
Write your guesses in here, if they are correct, you get a point.''')

while len(states_guessed) < 50:
    guess = screen.textinput(f"{len(states_guessed)}/50 States Correct", "What's Your Next Guess?").title()
    for state in states_csv.state:
        if guess == state:
            states_guessed.append(guess)
            correct_answer = states_csv[states_csv.state == guess]
            x = int(correct_answer.x)
            y = int(correct_answer.y)
            turtle.goto(x, y)
            turtle.write(f"{guess}", font=FONT)
    if guess == "Exit":
        states_to_learn = [state for state in states_csv.state if state not in states_guessed]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break







screen.exitonclick()