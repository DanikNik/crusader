#!/usr/bin/python

from pygame import *

class Block(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.width = 32
        self.height = 32
        self.color = '#96a3bf'
        self.image = Surface((self.width, self.height))
        self.image.fill(Color(self.color))
        self.rect = Rect((x, y, self.width, self.height))
        
