import turtle
import random
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple','pink']
#seatheading: 180 going back and 0 going front

def left_turn():
  t.setheading(180)
  
def right_turn():
  t.setheading(0)
  
def up_turn():
	t.setheading(90)
def down_turn():
	t.setheading(270)
  
def octagon():
  t.pensize(1)
  t.pencolor('white')
  t.fillcolor(random.choice(colors))
  t.speed('fastest')
  t.begin_fill() 

  for i in range(8):
    t.forward(10)
    t.left(45)
  t.end_fill()
  t.forward(40)
  
def left_start():
  for i in range (10):
    left_turn()
    octagon()
  up_turn()
  t.forward(30)
  
def right_start():
  for inde in range(10):
    right_turn()
    octagon()
  up_turn()
  t.forward(80)
  
for ind in range(4): 
  if ind%2==0:
    left_start()
  else:
    right_start()
    
t.done()