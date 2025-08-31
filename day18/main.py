import turtle
import random
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple','pink']

turtle.pensize(1)
turtle.pencolor('white')
turtle.fillcolor(random.choice(colors))
turtle.speed('normal')
turtle.begin_fill() 

for i in range(8):
    turtle.forward(100)
    turtle.left(45)
turtle.end_fill()
turtle.done()