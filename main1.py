# importing modules
from turtle import *
import random


race = False

# making a screen object with its attributes
my_screen = Screen()
my_screen.setup(width = 500, height = 400)
user_guess = my_screen.textinput(title="Make your guess", prompt="which turtle will win the race?Enter a color")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []

n = -150
r = -230
for i in range(7):
    rishi = Turtle(shape="turtle")
    rishi.penup()
    rishi.goto(x=r, y=n)
    rishi.color(colors[i])
    n += 50
    all_turtles.append(rishi)

if user_guess:
    race = True

while race:
    for i in all_turtles:
        random_distance = random.randint(0,10)
        i.forward(random_distance)

        if i.xcor() > 220:
            race = False

            winning_color = i.pencolor()

            if winning_color == user_guess:
                print(f"You won the game because you chose{winning_color}")
            else:
                print(f"you lost the game because the winner is {winning_color}")

my_screen.exitonclick()
