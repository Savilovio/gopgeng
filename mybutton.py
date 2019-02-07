# -*- coding: utf-8 -*-
import pygame
from pygame import *

def load_image(name, colorkey=None):
    image = pygame.image.load(name)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Button(pygame.sprite.Sprite):
    """Class used to create a button, use setCords to set 
        position of topleft corner. Method pressed() returns
        a boolean and should be called inside the input loop."""
    def __init__(self,image_name, ax, ay):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(image_name, -1)
        self.rect.topleft = ax, ay
        
    def setCords(self,x,y):
        self.rect.topleft = x,y

    def pressed(self,mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False
            
    def pos_obj(self, x, y):
        return self.rect.collidepoint(x,y)
