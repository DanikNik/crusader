#!/usr/bin/python

from pygame import *

MOVE_SPEED = 7
WIDTH = 32
HEIGHT = 32
PLAYER_COLOR = '#864242'

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startx = x
        self.starty = y
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(PLAYER_COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right, up, down):
        if left:
            self.xvel = -MOVE_SPEED

        if right:
            self.xvel = MOVE_SPEED

        if not(left or right):
            self.xvel = 0

        if up:
            self.yvel = -MOVE_SPEED

        if down:
            self.yvel = MOVE_SPEED

        if not(up or down):
            self.yvel = 0

        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
