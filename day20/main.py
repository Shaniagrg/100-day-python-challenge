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
    
    def __init__(self, shape, color, speed, x, y):
        self.snake = turtle.Turtle()
        self.shape = shape
        self.color = color
        self.speed = speed
        self.direction = "stop"  # Initial direction
        self.x = x  
        self.y = y
        self.position = self.snake_position(x,y)
        self.segments = []
    
    def snake_position(self,x,y):
        self.snake.up()
        self.snake.shape(self.shape)
        self.snake.setposition(x,y)
        self.snake.color(self.color)
        
    def set_arena_dimensions(self,arena_width,arena_height):
        self.arena_width = arena_width
        self.arena_height = arena_height
            
    def move_snake(self):
        #move body
        if self.direction == "right":
            self.x = self.x + 20 #move right until width 500
            
        if self.direction == "left":
            self.x = self.x - 20 #move left until width 500
            
        if self.direction == "up":
            self.y = self.y + 20 #move up until lenght 500
            
        if self.direction == "down":
            self.y = self.y - 20 #move down until length 500
        
        #setx() method is used to set the turtle's x-coordinate to a new value via for y
        self.snake.setx(self.x)  # Move the snake to the updated x position
        self.snake.sety(self.y)  # Move the snake to the updated y position
        
        
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
        self.boundry_check()
            
    def boundry_check(self):
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
        self.direction = "up"
        
    def go_down(self):
        self.direction = "down"
        
    def go_left(self):
        self.direction = "left"
        
    def go_right(self):
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
    
    arena = None
    snake_head = None
    food = None
    score = 0
   
    @classmethod
    def game_over(cls):
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.color("red")
        pen.goto(0, 0)
        pen.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    @classmethod
    def onkey_movement(cls):
        '''
        Set up controls
        screen.onkey(func, "Key") = it binds a key press to run a function.
        '''
        screen = cls.arena.screen
        screen.listen()
        screen.onkey(cls.snake_head.go_up, "Up")
        screen.onkey(cls.snake_head.go_down, "Down")
        screen.onkey(cls.snake_head.go_left, "Left")
        screen.onkey(cls.snake_head.go_right, "Right")
        
    @classmethod
    def create_food(cls):
        cls.food = Food(shape = "circle",color = "red")
        
    @classmethod
    def create_snake(cls):
        cls.snake_head = Snake(shape = "square", color = "white", speed = 0, x = 0, y = 0)
        
    @classmethod
    def create_arena(cls):
        cls.arena = Arena(width = 500, height = 500, bg_color = "black")
        cls.arena.setup_screen()

    @classmethod
    def start(cls):
        cls.create_arena()
        cls.create_snake()
        cls.create_food()
        cls.snake_head.set_arena_dimensions(cls.arena.width / 2, cls.arena.height / 2)
        cls.onkey_movement()
        
        while True:
            cls.snake_head.move_snake()
            if (cls.snake_head.x >= cls.arena.width/2 or cls.snake_head.x <= -cls.arena.width/2 or cls.snake_head.y >= cls.arena.height/2 or cls.snake_head.y <= -cls.arena.height/2):
                cls.game_over()
                break
            
            
        
        
Game.start()