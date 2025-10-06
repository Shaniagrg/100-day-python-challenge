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
    def __init__(self, shape, length, width, color, speed, x, y):
        self.snake = turtle.Turtle()
        self.shape = shape
        self.length = length
        self.width = width
        self.color = color
        self.speed = speed
        self.position = self.snake_position(x,y)
    
    def snake_position(self,x,y):
        self.snake.up()
        self.snake.shape(self.shape)
        self.snake.setposition(x,y)
        self.snake.color(self.color)
        
    '''
    
    def move_snake(self):
        if direction == "right":
            self.x = self.x + 1 #move right until width 500
        if direction == "left":
            self.x = self.x - 1 #move left until width 500
        if direction == "up":
            self.y = self.y + 1 #move up until lenght 500
        if direction == "down":
            self.y = self.y - 1 #move down until length 500'''
   
class Food:
    def __init__(self, shape, color, food_x, food_y):
        self.food = turtle.Turtle()
        self.shape = shape
        self.color = color
        self.position = self.food_position(x=food_x, y=food_y)
        
    def food_position(self,x,y):
        self.food.up()
        self.food.setposition(x,y)
        self.food.shape(self.shape)
        self.food.color(self.color)
class Game:
    @classmethod
    def create_food(cls):
        cls.food = Food(shape = "circle",color = "red", food_x = -50, food_y = 30)
    @classmethod
    def create_snake(cls):
        cls.snake = Snake(shape = "square", length=40, width = 10, color = "green", speed = 0, x = 0, y = 0)
    @classmethod
    def create_arena(cls):
        cls.arena = Arena(width = 500, height = 500, bg_color = "lavender")
        cls.arena.setup_screen()

    @classmethod
    def start(cls):
        cls.create_arena()
        cls.create_snake()
        cls.create_food()
        
        
Game.start()