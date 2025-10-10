'''
Snake

Feature:
    - lenght
    - width

Function:
    - movement x-axis and y-axis
'''

import turtle
import random

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
    def __init__(self, shape, length, width, color, speed, x, y, arena_width, arena_height):
        self.snake = turtle.Turtle()
        self.shape = shape
        self.length = length
        self.width = width
        self.color = color
        self.speed = speed
        self.direction = "stop"  # Initial direction
        self.arena_width = arena_width
        self.arena_height = arena_height
        self.x = x  
        self.y = y
        self.position = self.snake_position(x,y)
    
    def snake_position(self,x,y):
        self.snake.up()
        self.snake.shape(self.shape)
        self.snake.setposition(x,y)
        self.snake.color(self.color)
        
    
    def move_snake(self):
        if self.direction == "right":
            self.x = self.x + 1 #move right until width 500
        if self.direction == "left":
            self.x = self.x - 1 #move left until width 500
        if self.direction == "up":
            self.y = self.y + 1 #move up until lenght 500
        if self.direction == "down":
            self.y = self.y - 1 #move down until length 500
        
        #setx() method is used to set the turtle's x-coordinate to a new value via for y
        self.snake.setx(self.x)  # Move the snake to the updated x position
        self.snake.sety(self.y)  # Move the snake to the updated y position
        
        # Boundary checking 
        '''
        arena has 4 sides
        x = 2 sides which includes + and -
        y = 2 sides which includes + and -
        width = 500
        lenght = 500
        
        so width and lenght is divide 2 so each sides has equal part
        width is x whhich has 2 sides
        length is y which has 2 sides
        
        therefore we dont check for 500 width and lenght rather 500/2 = 250 
        
        '''
        if self.x > self.arena_width:  
            self.x = self.arena_width 
            self.snake.setx(self.x)  # Keep the snake at the boundary
        elif self.x < -self.arena_width:  
            self.x = -self.arena_width  
            self.snake.setx(self.x)
        if self.y > self.arena_height: 
            self.y = self.arena_height  
            self.snake.sety(self.y)
        elif self.y < -self.arena_height:  
            self.y = -self.arena_height 
            self.snake.sety(self.y)
    
    # Direction control
    
    def go_up(self): 
        if self.direction != "down":
            self.direction = "up"
    def go_down(self):
        if self.direction != "up":
            self.direction = "down"
    def go_left(self):
        if self.direction != "right":
            self.direction = "left"
    def go_right(self):
        if self.direction != "left":
            self.direction = "right"
class Food:
    def __init__(self, shape, color):
        self.food = turtle.Turtle()
        self.shape = shape
        self.color = color
        self.position = self.food_position(x=random.randint(-250,250), y=random.randint(-250,250))
        
    def food_position(self,x,y):
        self.food.up()
        self.food.setposition(x,y)
        self.food.shape(self.shape)
        self.food.color(self.color)
class Game:
    @classmethod
    def create_food(cls):
        cls.food = Food(shape = "circle",color = "red")
    @classmethod
    def create_snake(cls):
        cls.snake = Snake(shape = "square", length=40, width = 10, color = "green", speed = 0, x = 0, y = 0, arena_width = 500/2, arena_height = 500/2)
    @classmethod
    def create_arena(cls):
        cls.arena = Arena(width = 500, height = 500, bg_color = "lavender")
        cls.arena.setup_screen()

    @classmethod
    def start(cls):
        cls.create_arena()
        cls.create_snake()
        cls.create_food()
        # Set up controls
        #screen.onkey(func, "Key") = it binds a key press to run a function.
        screen = cls.arena.screen
        screen.listen()
        screen.onkey(cls.snake.go_up, "Up")
        screen.onkey(cls.snake.go_down, "Down")
        screen.onkey(cls.snake.go_left, "Left")
        screen.onkey(cls.snake.go_right, "Right")
        
        while True:
            cls.snake.move_snake()
        
        
Game.start()