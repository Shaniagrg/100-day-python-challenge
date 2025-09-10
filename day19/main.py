import turtle
import random
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
colors = ['red', 'orange', 'blue', 'green', 'purple','pink']
class Field:
    f = 0
    l = 0
    def __init__(self, forward=250, left=90):
        self.f = forward
        self.l = left 

    def size_field(self):
        for i in range(4):
            t.forward(self.f)
            t.left(self.l)

class Start:
    Field.f1 = None
    def __init__(self):
        self.f1 = Field()   # create a field

    def field_1(self):
        self.f1.size_field()   # draw the field
        
def players():
    t.pencolor(random.choice(colors))
    for i in range(50):
        t.forward(10 + i)
        t.left(91)

#players()
game = Start()
game.field_1()   
    
t.done()