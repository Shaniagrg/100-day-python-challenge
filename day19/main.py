import turtle
import random

width = 700
height=500
s=turtle.Screen()
s.setup(width,height)
s.bgcolor("lightgreen")
used_color = []
used_speed = []
players = {}
turtle_y_position = 10
line = 140
user = input("Which color do you think will win?: ")
#create pen
t = turtle.Turtle()
t.speed(0)
t.hideturtle() #hide the cursor
class Arena:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()

    def start_line(self):
        self.t.up()  # Lift the pen
        self.t.setposition(-140, 50)
        self.t.write("start line", align='center')
        self.t.right(90)  # Face forward down
        self.t.forward(10)
        self.t.down()  # Put the pen down
        self.t.forward(155)

    def finish_line(self):
        self.t.up()  # Lift the pen
        self.t.setposition(140, 50)
        self.t.write("finish line", align='center')
        self.t.forward(10)
        self.t.down()  # Put the pen down
        self.t.forward(155)

    def track_line(self):  
        yposition = 20
        self.t.left(90)  # Face to the left
        for i in range(5):
            self.t.up()
            self.t.setposition(-170, yposition)
            self.t.color("white")
            self.t.down()
            self.t.forward(340)
            yposition = yposition - 25  

    def draw_track(self):
        self.start_line()  # Corrected method names to call all function
        self.finish_line()  
        self.track_line()  

class Players():
    def __init__(self):
        self.t1 = turtle.Turtle()
        self.colors = ['red', 'orange', 'blue', 'green', 'purple']
        self.speed_list = [ 1,2,3,4,5]
    def turtle_position(self):
        global turtle_y_position  # Declare turtle_y_position as global
        self.t1.up()
        self.t1.setposition(-160,turtle_y_position)
        self.t1.shape("turtle")
        self.t1.color(self.color())
        #t1.speed(self.speed())
        turtle_y_position = turtle_y_position - 25
        
    def color(self):
        chosen_color = random.choice(self.colors)
        while chosen_color in used_color:  # gets used_colors from global frame
            chosen_color = random.choice(self.colors)
        used_color.append(chosen_color)
        return chosen_color
    
    def speed(self):
        chosen_speed = random.choice(self.speed_list)
        while chosen_speed in used_speed:  # gets used_speed from global frame
            chosen_speed = random.choice(self.speed_list)
        used_speed.append(chosen_speed)
        return chosen_speed

class Start():
    def __init__(self):
        self.tom = Players()
        self.harry = Players()
        self.tim = Players()
        self.rita = Players()
        self.wendy = Players()
        
    def game_play(self):
        f1 = Arena()
        f1.draw_track()
        self.tom.turtle_position()
        self.harry.turtle_position()
        self.tim.turtle_position()
        self.rita.turtle_position()
        self.wendy.turtle_position()
        
    def assign_speed(self):
        # Assign speeds to each player
        tom_speed = self.tom.speed()
        harry_speed = self.harry.speed()
        tim_speed = self.tim.speed()
        rita_speed = self.rita.speed()
        wendy_speed = self.wendy.speed()

        # Move turtles until one crosses the finish line
        while (self.tom.t1.xcor() < line and 
               self.harry.t1.xcor() < line and 
               self.tim.t1.xcor() < line and 
               self.rita.t1.xcor() < line and 
               self.wendy.t1.xcor() < line):
            self.tom.t1.forward(tom_speed)
            self.harry.t1.forward(harry_speed)
            self.tim.t1.forward(tim_speed)
            self.rita.t1.forward(rita_speed)
            self.wendy.t1.forward(wendy_speed)

        #final_list = [tom.xcor(), harry.xcor(), tim.xcor(), rita.xcor(), wendy.xcor()]
        #final_dict = {tom.xcor():used_color[0], harry.xcor():used_color[1], tim.xcor():used_color[2], rita.xcor():used_color[3], wendy.xcor():used_color[4]}
    
    def play(self):
        self.game_play()
        self.assign_speed()
    
game = Start()
game.play()

t.done()      
turtle.done()