import turtle
import random
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
colors = ['red', 'orange', 'blue', 'green', 'purple','pink']

def players():
    t.pencolor(random.choice(colors))
    for i in range(50):
        t.forward(10 + i)
        t.left(91)

players()
    
t.done()