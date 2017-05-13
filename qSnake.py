# Snake game using OOP

from Tkinter import *

class Snake(object):

    def __init__(self, x, y, window):
        # initialize snake
        # initialize position (x,y)
        # create head
        # create body

    def eat_food(self, food):
        # remove food
        # increase body
        # increase score
        # increase speed

    def update(self):
        # update snake position/move

    def render(self):
        # draw snake in console using curses

    def move(self):
        # move the snake

class Body(object):

    def __init__(self, x, y, char="#"):
        self.x = x
        self.y = y
        self.char = char

    @property
    def coor(self):
        return self.x, self.y

class Food(object):
    def __init__(self, window, char="#"):
        # set random x, y position
    def render(self):
        # draw food to console

    def randomize(self):
        # randomize x, y position

if __name__ == '__main__':

    while True:
        # clear screen
        # display the snake
        # display the food
        # display the score
        # listen to keypress event
        # respond to keypress event
        # stop the game if head hits the body/eats itself/dies
