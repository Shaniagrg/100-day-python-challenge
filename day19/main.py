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
        self.start_line()  
        self.finish_line()  
        self.track_line()  

a = Arena(length=155, track_length=340, width=700, height=500, bg_color="lightgreen", x=140, y=50, angle=90)
a.screen()  # Set up the screen
a.draw_track()  # Draw the track

#Start.create_arena()

turtle.done()