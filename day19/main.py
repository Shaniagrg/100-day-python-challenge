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

class Players:
    def player(self):
        t.pencolor(random.choice(colors))
        #t.penup(40)
        for i in range(30):
            t.forward(1 + i)
            t.left(91)
            
class Start:
    Field.f1 = None
    Players.p = None
    def __init__(self):
        self.f1 = Field()   # create a field
        self.p = Players() 
         
    def field_1(self):
        self.f1.size_field()   # draw the field
        self.p.player() 
        
game = Start()
game.field_1()   
    
t.done()