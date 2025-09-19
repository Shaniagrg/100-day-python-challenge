import turtle
import random

#create pen
t = turtle.Turtle()

class Arena:
    
    def __init__(self, length, track_length, width, height, bg_color, x, y, angle):
        self.length = length
        self.track_length = track_length
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.angle = angle
        
    def screen(self):
        s = turtle.Screen()
        s.setup(self.width, self.height)
        s.bgcolor(self.bg_color)
        
    def start_line(self):
        x_axis = -self.x
        t.up()  # Lift the pen
        t.setposition(x_axis, self.y)
        t.write("start line", align='center')
        t.right(self.angle)  # Face forward down
        t.forward(10)
        t.down()  # Put the pen down
        t.forward(self.length)
        t.hideturtle()

    def finish_line(self):
        t.up()  # Lift the pen
        t.setposition(self.x, self.y)
        t.write("finish line", align='center')
        t.forward(10)
        t.down()  # Put the pen down
        t.forward(self.length)
        t.hideturtle()

    def track_line(self):  
        yposition = 20
        xposition = -self.x - 30
        t.left(self.angle)  # Face to the left
        for i in range(5):
            t.up()
            t.setposition(xposition, yposition)
            t.color("white")
            t.down()
            t.forward(self.track_length)
            yposition = yposition - 25  
            t.hideturtle()

    def draw_track(self):
        self.screen()
        self.start_line()  
        self.finish_line()  
        self.track_line()  

class Player:
    def __init__(self, name = '', color='white', speed=0.0, x = 0):
        self.name = name
        self.color = color
        self.speed = speed
        self.x = x
        
    def turtle_position(self):
        t1 = turtle.Turtle()
        global turtle_y_position  # Declare turtle_y_position as global
        t1.up()
        t1.setposition(self.x,turtle_y_position)
        t1.shape("turtle")
        t1.color(self.color)
        turtle_y_position = turtle_y_position - 25
        
      
colors = ['red', 'orange', 'blue', 'green', 'purple']
player_name = ["p1","p2","p3","p4","p5"]
players = []
a = Arena(length=155, track_length=340, width=700, height=500, bg_color="lightgreen", x=140, y=50, angle=90)
a.draw_track()  # Draw the track
turtle_y_position = 10

for i in range(5):
    p = Player(name = player_name[i], color = colors[i], speed = random.uniform(0,5), x = -160)
    players.append(p)
    p.turtle_position()


#Start.create_arena()

turtle.done()