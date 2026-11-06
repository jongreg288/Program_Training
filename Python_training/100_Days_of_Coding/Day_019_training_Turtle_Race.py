import turtle
import tkinter as tk
import random

#screen control
screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("#7ec850")
screen.setup(width=800, height=600)
turtle.bgpic("Python_training\\Additional_Assets\\turtle_track.png")

# I don't know a better way to pull 7 turtles of different colours yet, so, I'm creating them manually.
# I actually realized I can create them in a loop, but for now, I'll keep it manual. The colour text in the background PNG is set.
Red = turtle.Turtle()
Red.color("red")
Red.shape("turtle")
Red.penup()
Red.goto(-225, 150)

Orange = turtle.Turtle()
Orange.color("orange")
Orange.shape("turtle")
Orange.penup()
Orange.goto(-225, 100)

Yellow = turtle.Turtle()
Yellow.color("yellow")
Yellow.shape("turtle")
Yellow.penup()
Yellow.goto(-225, 50)

Green = turtle.Turtle()
Green.color("green")
Green.shape("turtle")
Green.penup()
Green.goto(-225, 0)

Blue = turtle.Turtle()
Blue.color("blue")
Blue.shape("turtle")
Blue.penup()
Blue.goto(-225, -50)

Indigo = turtle.Turtle()
Indigo.color("indigo")
Indigo.shape("turtle")
Indigo.penup()
Indigo.goto(-225, -100)

Violet = turtle.Turtle()
Violet.color("violet")
Violet.shape("turtle")
Violet.penup()
Violet.goto(-225, -150)

# Pick the lucky turtle before the race starts
turtles = [Red, Orange, Yellow, Green, Blue, Indigo, Violet]
lucky = random.choice(turtles)
multipliers = {t: 1.0 for t in turtles}
multipliers[lucky] = 1.10
    
def get_player_count():
    player_count = None
    while player_count is None:
        player_count = turtle.numinput("Turtle Race", "Enter number of players,\n Or 0 to watch the race:", minval=0, maxval=7)
        if player_count != int(player_count): # I learned after this that turtle or tkinter has its own way to handle non-integer input.
            turtle.textinput("Turtle Race", "That's not an integer. Enter an integer (number) between 0 and 7.")
        elif player_count < 0 or player_count > 7:
            turtle.textinput("Turtle Race", "Invalid number of players. Enter a number between 0 and 7.")
    return player_count

def get_color_pick():
    color_picks = []
    i = 0
    if player_count == 0:
        color_picks = [lucky.color()[0].lower()]
        return color_picks
    else:
        while i < int(player_count):
            color_pick = turtle.textinput("Turtle Race", "Player " + str(i+1) + ", Enter your winning pick:")
            while color_pick.lower() not in ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]:
                color_pick = turtle.textinput("Turtle Race", "Invalid entry.\n Please enter your winning pick:")
            color_picks.append(color_pick)
            i += 1
        return color_picks

def race():
    global turtles
    while True:
        for t in turtles:
            t.forward(random.randint(1, 5) * multipliers[t])
            if t.xcor() > 200:
                if player_count == 0:
                    turtle.TK.messagebox.showinfo("Turtle Race", t.color()[0].capitalize() + " turtle won!\n The Lucky Turtle was " + lucky.color()[0].capitalize() + ".")
                else:
                    if t.color()[0] == color_picks[0].lower():
                        turtle.TK.messagebox.showinfo("Turtle Race", "Player " + str(color_picks.index(t.color()[0].lower()) + 1) + " won!\n The Lucky Turtle was " + lucky.color()[0].capitalize() + ".")
                    else:
                        turtle.TK.messagebox.showinfo("Turtle Race", "No winners!\n The Lucky Turtle was " + lucky.color()[0].capitalize() + ".")
                return

player_count = get_player_count()
color_picks = get_color_pick()
race()
turtle.done()