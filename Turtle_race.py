import turtle
import time
import random

"""IMPORTANT MESSAGE!!!
    You should use computer main terminal.
    Or else Your Turtle window can't show on screen."""

WIDTH, HEIGHT = 1000, 700
COLORS = [
    "red",
    "green",
    "blue",
    "yellow",
    "black",
    "pink",
    "brown",
    "cyan",
    "purple",
    "orange",
]


def get_number_from_user():
    racers = 0
    while True:
        racers = input("Enter the number of racers(2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Enter a valid number!!!!!!!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Enter the number between (2 to 10)!!!!!!!!! ")


def race(colors):
    turtles = create_turtle(colors)

    while True:
        for racer in turtles:
            steps = random.randrange(1, 20)
            racer.forward(steps)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtle(colors):
    turtles = []
    specingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * specingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing!")


racers = get_number_from_user()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"The Winner is {winner}.")
time.sleep(5)
