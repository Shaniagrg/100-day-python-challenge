import turtle
import random
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple','pink']

for i in range(0,10,1):
    turtle.pensize(1)
    turtle.pencolor('white')
    turtle.fillcolor(random.choice(colors))
    turtle.speed('fastest')
    turtle.begin_fill() 

    for i in range(8):
        turtle.forward(20)
        turtle.left(45)
    turtle.end_fill()
    turtle.forward(70)
    turtle.done()