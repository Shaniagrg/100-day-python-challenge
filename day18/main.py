import turtle
turtle.pensize(4)
turtle.pencolor('blue')
turtle.fillcolor('blue')
turtle.speed('normal')
turtle.begin_fill() 

for i in range(8):
    turtle.forward(100)
    turtle.left(45)
turtle.end_fill()
turtle.done()