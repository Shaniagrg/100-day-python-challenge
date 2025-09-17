import turtle
import random

t = turtle.Turtle()
t.speed(0)  # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
y_axis = [215, 172, 129, 86, 43, 0]
used_colors = []  # Corrected variable name

class Arena:
    def __init__(self, forward=250, left=90):
        self.f = forward
        self.l = left 

    def size_field(self):
        for i in range(4):  # make square
            t.forward(self.f)
            t.left(self.l)

class Players:
    def __init__(self, r=12):
        self.radius = r
        self.colors = ['red', 'orange', 'blue', 'green', 'purple']

    def player(self, x, y):
        t.penup()
        t.goto(x, y)
        t.fillcolor(self.color())  # Corrected to use self.color()
        t.begin_fill() 
        t.circle(self.radius)
        t.end_fill() 

    def color(self):
        chosen_color = random.choice(self.colors)
        while chosen_color in used_colors:  # Use the global list
            chosen_color = random.choice(self.colors)
        used_colors.append(chosen_color)
        return chosen_color
    
    def player_race(self):
        # Implement race logic here
        pass

class Starts:
    def __init__(self):
        self.players = []

    def game_play(self):
        f1 = Arena()
        f1.size_field()
        
        # Call player_race to start the race if implemented
        # p.player_race()

game = Starts()
game.game_play()
def gap():
    t.setheading(90)
    t.forward(40)
tom = Players()   
gap()
tom.player(x=40, y=y_axis[0])

harry = Players()   
gap()
harry.player(x=40, y=y_axis[1])

tim = Players()   
gap()
tim.player(x=40, y=y_axis[2])

rita = Players()   
gap()
rita.player(x=40, y=y_axis[3])

wendy = Players()   
gap()
wendy.player(x=40, y=y_axis[4])

t.done()