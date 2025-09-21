import turtle
import random

class Arena:
    
    def __init__(self, speed, length, track_length, width, height, bg_color, x, y, angle, track_yposition, track_xposition, track_color):
        self.pen = turtle.Turtle()  #create pen
        self.screen = turtle.Screen()
        self.speed = speed
        self.length = length
        self.track_length = track_length
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.x = x
        self.y = y
        self.angle = angle
        self.track_yposition = track_yposition
        self.track_xposition = track_xposition
        self.track_color = track_color
        
    def setup_screen(self):
        self.screen.setup(self.width, self.height)
        self.screen.bgcolor(self.bg_color)
        
    def start_line(self):
        x_axis = -self.x
        self.pen.up()  #Lift the pen
        self.pen.speed(self.speed)
        self.pen.setposition(x_axis, self.y)
        self.pen.write("start line", align='center')
        self.pen.right(self.angle)  # Face forward down
        self.pen.forward(10)
        self.pen.down()  # Put the pen down
        self.pen.forward(self.length)

    def finish_line(self):
        self.pen.up()  # Lift the pen
        self.pen.speed(self.speed)
        self.pen.setposition(self.x, self.y)
        self.pen.write("finish line", align='center')
        self.pen.forward(10)
        self.pen.down()  # Put the pen down
        self.pen.forward(self.length)

    def track_line(self):  
        self.pen.speed(self.speed)
        self.pen.left(self.angle)  # Face to the left
        for i in range(5):
            self.pen.up()
            self.pen.setposition(self.track_xposition, self.track_yposition)
            self.pen.color(self.track_color)
            self.pen.down()
            self.pen.forward(self.track_length)
            self.track_yposition = self.track_yposition - 25  
            self.pen.hideturtle()

    def draw_track(self):
        self.setup_screen()
        self.start_line()  
        self.finish_line()  
        self.track_line()  

class Player:
    def __init__(self, name = '', shape = "", color='white', speed=0.0, turtle_x_position = 0, turtle_y_position = 0):
        self.each_player = turtle.Turtle()
        self.name = name
        self.shape = shape
        self.color = color
        self.speed = speed
        self.position = self.turtle_position(turtle_x_position,turtle_y_position)
        
    def turtle_position(self,x,y):
        self.each_player.up()
        self.each_player.setposition(x,y)
        self.each_player.shape(self.shape)
        self.each_player.color(self.color)
        
    def move(self):
        self.each_player.forward(self.speed)
      
      
class Game:
    players = []  #type: list[Player]
    colors = ['red', 'orange', 'blue', 'green', 'purple']  #type: list[str]
    names = ['p1', 'p2', 'p3', 'p4', 'p5'] #type: list[str]
    arena = None  #arena: Arena = None
    winner = None   #winner: str = None
    line = 140
    #user = input("Which color do you think will win?: ")

    @classmethod
    def display_winner(cls):
        # Display the winner on the screen
        cls.arena.pen.up()  
        cls.arena.pen.setposition(0, 80)  # Move to the center of the screen
        cls.arena.pen.write("The winner is: {}".format(cls.winner), align='center', font=("Arial", 16, "bold"))
        cls.arena.pen.hideturtle()  

    @classmethod
    def race_turtle(cls):
        while True:
            for index in cls.players:
                index.move()  # Move each player
                # Check if the player has reached the finish line
                if index.each_player.xcor() >= cls.line:
                  cls.winner = index.name
                  cls.display_winner()
                  return  # Exit the loop once a winner is found

    @classmethod
    def create_players(cls):
        assigned_speeds = set()
        locate_turtle = 22
        for i in range(5):
            player_name = cls.names[i]
            player_color = cls.colors[i]
            
            player_speed = random.uniform(0,5)
            while player_speed in assigned_speeds:
                player_speed = random.uniform(0, 5)
            assigned_speeds.add(player_speed)
            
            p = Player(name=player_name, shape="turtle", color=player_color, speed=player_speed, turtle_x_position=-160, turtle_y_position = locate_turtle)
            cls.players.append(p)
            locate_turtle = locate_turtle - 25
            

    @classmethod
    def create_arena(cls):
        cls.arena = Arena(speed = 0, length=155, track_length=340, width=700, height=500, bg_color="lightgreen", x=140, y=50, angle=90, track_yposition = 10, track_xposition = -160, track_color = "white")
        cls.arena.draw_track()

    @classmethod
    def start(cls):
        cls.create_arena()
        cls.create_players()
        cls.race_turtle()
        turtle.done()


# Run the game
Game.start()  
