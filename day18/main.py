import turtle
import random
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple','pink']
#seatheading: 180 going back and 360 going front

def left_turn():
  turtle.setheading(180)
  turtle.forward(10)
  
def right_turn():
  turtle.setheading(360)
  turtle.forward(10)

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
for i in range (0,4,1):
    for i in range(0,10,1):
        octagon()
        left_turn()

    for i in range(0,10,1):
        octagon()  
        right_turn() 
turtle.done()