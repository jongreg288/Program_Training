from tracemalloc import start
import turtle
import math
import random

#screen control
sc = turtle.Screen()
sc.bgcolor('CadetBlue2')
sc.listen()

#player control
player = turtle.Turtle()
player.color('tomato')
player.shape('arrow')
speed = 6

#movement control
#comment out from here to see the assignment in action
"""def move_player():
    player.forward(speed)

def up():
    player.seth(90)
    move_player()

def down():
    player.seth(270)
    move_player()

def right():
    player.seth(0)
    move_player()

def left():
    player.seth(180)
    move_player()

#toggle pen state
def toggle_pen():
    if player.isdown():
        player.penup()
    else:
        player.pendown()
        
sc.onkey(toggle_pen, "space")

sc.onkeypress(key='w', fun=up)
sc.onkeypress(key='s', fun=down)
sc.onkeypress(key='d', fun=right)
sc.onkeypress(key='a', fun=left)"""

#this portion draws polygons of increasing side count. 
"""c = 4
s = 4

while s < 11:
    for i in range(c):
        turtle.colormode(255)
        player.forward(100)
        player.left(360/s)
        player.color(random.choice(range(0, 255)), random.choice(range(0, 255)), random.choice(range(0, 255)))
        c += 1
    s += 1
    c = s"""

#this portion will draw a spirograph.
"""start = player.pos()
player.speed(0)
i = 0

while i < 100:
    if player.distance(start) < 1:
        player.circle(math.asin(1/math.sqrt(2))*100)
    player.right(math.pi*math.sqrt(2))

    i += 1
"""
turtle.done() #keeps the window open, use the close button to exit the program
