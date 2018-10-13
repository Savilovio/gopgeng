from pygame import *
import pyganim


MOVE_SPEED = 30
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
ANIMATION_DELAY = 1
ANIMATION_RIGHT = [('image/anim/r0.png'),
            ('image/anim/r1.png'),
            ('image/anim/r2.png')]
ANIMATION_LEFT = [('image/anim/l0.png'),
            ('image/anim/l1.png'),
            ('image/anim/l2.png')]
ANIMATION_STAY = [('image/anim/r0.png', ANIMATION_DELAY)]
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        self.image = image.load ("image/heros/hero.jpg") 
        self.rect = Rect(x, y, WIDTH, HEIGHT)
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
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))
        self.boltAnimJumpLeft= pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()      
        self.boltAnimJumpRight= pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()
        
        self.boltAnimJump= pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
    def update(self, left, right, up, platforms): 
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.image.fill(Color(COLOR))
                self.boltAnimJump.blit(self.image, (0, 0))
        if left:
            self.xvel = -MOVE_SPEED 
            self.image.fill(Color(COLOR))
        if right:
            self.xvel = MOVE_SPEED 
            self.image.fill(Color(COLOR))
        if not(left or right):
            self.xvel = 0
        if not self.onGround:
            self.yvel += GRAVITY

            self.onGround = False 
            self.rect.y += self.yvel
            self.collide(0, self.yvel, platforms)

            self.rect.x += self.xvel
            self.collide(self.xvel, 0, platforms)
            self.boltAnimJump.blit(self.image, (0, 0))

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom 
                    self.yvel = 0
