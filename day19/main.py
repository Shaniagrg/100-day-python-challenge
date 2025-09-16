import turtle
import random
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
y_axis = [215, 172, 129, 86, 43, 0]
players_color = []
speed = [1,3,5,10,0]
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
    #speed = 0
    colors = []
    def __init__(self,r=12):
        self.radius = r
        #self.speed = s
        self.colors = ['red', 'orange', 'blue', 'green', 'purple']
    def player(self,x,y):
        #t.speed(self.speed)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.pencolor('white')
        chosen_color = random.choice(self.colors)
        while chosen_color in players_color:
            chosen_color = random.choice(self.colors)
        players_color.append(chosen_color)
        t.fillcolor(chosen_color)
        
        t.begin_fill() 
        t.circle(self.radius)
        t.end_fill() 
    
            
class Start:
    def game_play(self):
        f1 = Arena()
        f1.size_field()
        p = Players()
        for i in range (5):
            t.setheading(90)
            t.forward(40)
            p.player(x=40,y=y_axis[i])
            
        
game = Start()
game.game_play()   
    
t.done()