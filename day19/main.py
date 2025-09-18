import turtle
width = 700
height=500
s=turtle.Screen()
s.setup(width,height)
s.bgcolor("lightgreen")

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

    def track_line(self):  # Added 'self' parameter
        yposition = 20
        self.t.left(90)  # Face to the left
        for i in range(5):
            self.t.up()
            self.t.setposition(-170, yposition)
            self.t.color("white")
            self.t.down()
            self.t.forward(340)
            yposition = yposition - 25  # Use shorthand for decrementing

    def draw_track(self):
        self.start_line()  # Corrected method names
        self.finish_line()  # Corrected method names
        self.track_line()  # Corrected method names

# Create an instance of the Arena class and draw the track
game = Arena()
game.draw_track()

turtle.done()