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

class Game:
    @classmethod
    def create_arena(cls):
        cls.arena = Arena(width = 500, height = 500, bg_color = "lavender")
        cls.arena.setup_screen()

    @classmethod
    def start(cls):
        cls.create_arena()
        
        
Game.start()