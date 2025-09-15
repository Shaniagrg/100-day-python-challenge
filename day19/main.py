import turtle
import random
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
colors = ['red', 'orange', 'blue', 'green', 'purple','pink']
class Arena:
    f = 0
    l = 0
    def __init__(self, forward=250, left=90):
        self.f = forward
        self.l = left 

    def size_field(self):
        for i in range(4): #make square
            t.forward(self.f)
            t.left(self.l)

class Players:
    radius = 0
    speed = 0
    colors = []
    def __init__(self,r=12, s=0):
        self.radius = r
        self.speed = s
        self.colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple','pink']
    def player(self):
        t.speed(self.speed)
        t.pencolor('white')
        t.fillcolor(random.choice(self.colors))
        t.begin_fill() 
        t.circle(self.radius)
        t.end_fill() 
            
class Start:
    Arena.f1 = None
    Players.p = None
    def __init__(self):
        self.f1 = Arena()   # create a field
        self.p = Players() 
         
    def field_1(self):
        self.f1.size_field()   # draw the field
        self.p.player() 
        
game = Start()
game.field_1()   
    
t.done()