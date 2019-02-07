# -*- coding: utf-8 -*-
from pygame import *
import pyganim


MOVE_SPEED = 50
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
JUMP_POWER = 50
GRAVITY = 3
ANIMATION_DELAY = 1
ANIMATION_RIGHT = [('image/anim/r1.png'),
            ('image/anim/r2.png')]
ANIMATION_LEFT = [('image/anim/l0.png'),
            ('image/anim/l1.png'),
            ('image/anim/l2.png')]
ANIMATION_STAY = [('image/anim/r0.png', ANIMATION_DELAY)]
ANIMATION_JUMP = [('image/anim/jr.png')]
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

class Player(sprite.Sprite):
    def __init__(self, x, y, image_filename):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        self.image = image.load (image_filename) 
        self.   rect = Rect(x, y, WIDTH, HEIGHT)
        self.yvel = 0
        self.onGround = False
        self.image.set_colorkey(Color(COLOR))
        
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()       
        boltAnim = []
        for anim in ANIMATION_LEFT:
             boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        boltAnim = []
        for anim in ANIMATION_JUMP:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimJump = pyganim.PygAnimation(boltAnim)
        self.boltAnimJump.play()


                
    def update(self, left, right, up, down): 
        #if go:
            
        if left:
            self.xvel = -MOVE_SPEED 
        if right:
            self.xvel = MOVE_SPEED             
        if up:
            self.yvel = JUMP_POWER
        if down:
            self.yvel = -JUMP_POWER
        if not (up or down or left or right):
            self.xvel = 0 
            self.yvel = 0

        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))

class Pistolet(Player):
    def set_center(self):
        cx = 0,5 * 55 
        cy = 0,5 * 55

    def __init__(self, x, y, image_filename):
        super().__init__(x, y, image_filename)
        self.set_center()

    def update(self, left, right, up, down):
        super().update(left, right, up, down)
        self.set_center()

