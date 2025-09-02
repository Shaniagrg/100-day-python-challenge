import turtle
import random
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple','pink']

def octagon():
    turtle.pensize(1)
    turtle.pencolor('white')
    turtle.fillcolor(random.choice(colors))
    turtle.speed('fastest')
    turtle.begin_fill() 

    for i in range(8):
        turtle.forward(10)
        turtle.left(45)
    turtle.end_fill()
    turtle.forward(40)

for i in range(0,10,1):
    octagon()
turtle.done()