
# -*- coding: utf-8 -*-
import easygui
from Player import*
import Player
import pygame
import object 
from pygame import *
from mybutton import* 
yellow    = (255, 255,   0)   
blue      = (  0,   0, 255)    
white     = (255, 255, 255) 
state_screen = 0 
def main():
    pygame.init()
    background_image = pygame.image.load('image/card/fon.jpg') # путь до картинки 
    WIN_WIDTH = 1000 #размеры
    WIN_HEIGHT = 800 #экрана
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # дисплкей по ширине и высоте 
    screen = pygame.display.set_mode(DISPLAY) # 
    screen.blit(background_image, (0, 0)) # 
    entities = pygame.sprite.Group()
    heros = pygame.sprite.Group()
    obj = pygame.sprite.Group()
    pygame.display.set_caption('Месть за братка ')
    pygame.display.update()#обновляем экран
# создаём надпись
    fontObj = pygame.font.Font('freesansbold.ttf', 22) # 
    textSurfaceObj = fontObj.render('Добро пожаловать в игру месть за брата . Для продолжения нажмите "Далее"  ', True, yellow, blue) # сама надпись  
    textRectObj = textSurfaceObj.get_rect() # 
    textRectObj.center = (400, 300) # размеры надписи

    screen.blit(textSurfaceObj, textRectObj)
    button = Button('image/card/button.jpg', 350, 400) #Button class is created
    music = pygame.mixer.music.load('musik/bitva.mp3')
    pygame.mixer.music.play(-1, 0.0)
 # размеры кнопки
    entities.add(button) # 
    entities.draw(screen) # 
    background_image = pygame.image.load("images/card.jpg")
    # задаём героя 
    heros.add(hero)
    hero = Player(55,55) 
    left = right = False 
    # делаем обьек из спрайта в строке 24 
    obj = object('image/gopniki/gop4.jpg')
    obj.add(object)

while 1:        
    for e in pygame.event.get():
        if e.type == QUIT:
            raise SystemExit, "QUIT"
        if e.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
        if state_screen == 1:
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
        if e.type == KEYUP and e.key == K_LEFT:
            left = False
        if e.type == KEYDOWN and e.key == K_RIGHT:
            right = True
        if e.type == KEYUP and e.key == K_RIGHT:
            right = False
        if e.type == KEYDOWN and e.key == K_UP:
            go = True
        if e.type == KEYUP and e.key == K_UP:
            go = False
        if e.type == KEYDOWN and e.key == K_DOWN:
            go_back = True
        if e.type == KEYUP and e.key == K_DOWN:
            go_back = False
            
            
        if state_screen == 0:                
                if button.pressed(mouse):
                    state_screen = 1   
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    heros.draw(screen)
                    pygame.display.flip()

        if state_screen == 1:
                if button.pressed(mouse):
                    state_screen = 2   
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    obj.draw(screen)
                    pygame.display.flip()