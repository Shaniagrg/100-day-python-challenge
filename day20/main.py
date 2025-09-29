'''
Snake

Feature:
    - lenght
    - width

Function:
    - movement x-axis and y-axis
'''

import turtle

class Arena:
    def __init__(self, height, width, bg_color):
        self.screen = turtle.Screen()
        self.height = height
        self.width = width
        self.bg_color = bg_color
        
    def setup_screen(self):
        self.screen.setup(self.width, self.height)
        self.screen.bgcolor(self.bg_color)

class Snake:
    def __init__(self, length, width, color, speed, x, y):
        self.snake = turtle.Turtle()
        self.length = length
        self.width = width
        self.color = color
        self.speed = speed
        self.position = self.snake_position(x,y)
    
    def snake_position(self,x,y):
        self.snake.up()
        self.snake.setposition(x,y)
        self.snake.color(self.color)
        self.draw_snake()
        
    def draw_snake(self):
        self.snake.speed(self.speed)
        self.snake.begin_fill()  # color fill
        for index in range(2):
            self.snake.forward(self.length)  
            self.snake.right(90)  
            self.snake.forward(self.width)  
            self.snake.right(90) 
        self.snake.end_fill()
        
class Game:
    @classmethod
    def create_snake(cls):
        cls.snake = Snake(length=40, width = 10, color = "green", speed = 0, x = 0, y = 0)
    @classmethod
    def create_arena(cls):
        cls.arena = Arena(width = 500, height = 500, bg_color = "lavender")
        cls.arena.setup_screen()

    @classmethod
    def start(cls):
        cls.create_arena()
        cls.create_snake()
        
        
Game.start()