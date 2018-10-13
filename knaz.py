# -*- coding: utf-8 -*-
import easygui

import pygame
from pygame import *
from mybutton import *

   
yellow    = (255, 255,   0)   
blue      = (  0,   0, 255)    
white     = (255, 255, 255)      
state_screen = 0   
# задаем параметры экрана
pygame.init()
background_image = pygame.image.load("images/zamok.jpg") # путь до картинки 
WIN_WIDTH = 800 #размеры
WIN_HEIGHT = 640 #экрана
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # дисплкей по ширине и высоте 
screen = pygame.display.set_mode(DISPLAY) # 
screen.blit(background_image, (0, 0)) # 
entities = pygame.sprite.Group() # 
images_hero = pygame.sprite.Group()
loc_go = pygame.sprite.Group()
heros_ad = pygame.sprite.Group()
goble_added = pygame.sprite.Group()
yov_ho = pygame.sprite.Group()
duck_map = pygame.sprite.Group()
final_arem = pygame.sprite.Group()
knaz_po = pygame.sprite.Group()
konez_vse = pygame.sprite.Group()
pygame.display.set_caption("TAH")

pygame.display.update()#обновляем экран
# создаём надпись
fontObj = pygame.font.Font('freesansbold.ttf', 22) # 
textSurfaceObj = fontObj.render('Welcome to Knaz game . SLAVA UKRAINE  ', True, yellow, blue) # сама надпись  
textRectObj = textSurfaceObj.get_rect() # 
textRectObj.center = (400, 300) # размеры надписи

screen.blit(textSurfaceObj, textRectObj)
button = Button('images/button.jpg', 350, 400) #Button class is created
 # размеры кнопки
entities.add(button) # 
entities.draw(screen) # 

textSurfaceObj = fontObj.render(' You Politikal Putana . Strong 9 , adroitness 4 , luck 7', True, yellow, blue)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (400, 350)
screen.blit(textSurfaceObj, textRectObj)

card_hero = Button('images/button1.jpg', 400, 300)
hero1_hero = Button('images/hero1.jpg', 50, 200)
images_hero.add(card_hero)
images_hero.add(hero1_hero)

background_image = pygame.image.load("images/card1.jpg")
cards_go = Button ("images/loc0.jpg",10, 250)
p_go = Button ("images/lok1.jpg",200, 230)
s_go = Button ("images/loc2.jpg",400, 300)
d_go = Button ("images/loc3.jpg",550, 450)
loc_go.add(cards_go)
loc_go.add(p_go)
loc_go.add(s_go)
loc_go.add(d_go)

h_ad  = Button ("images/king.jpg",0, 0)
h_added = Button ("images/babka.png",0, 0)
v_ho = Button ("images/monax.png",0, 0)
d_map = Button ("images/smertbabki.png", 0, 0)
f_arem = Button ("images/durak.png", 0, 0)
kn_po = Button ("images/Kvest1.png", 0, 0)
ko_vse = Button ("images/konez.png", 0, 0)
heros_ad.add(h_ad)
goble_added.add(h_added)
yov_ho.add(v_ho)
duck_map.add (d_map)
final_arem.add(f_arem)
knaz_po.add(kn_po)
konez_vse.add(ko_vse)
pygame.display.update()



# цикл ожидания нажатия 
while 1:        
    for e in pygame.event.get():
        if e.type == QUIT:
            raise SystemExit, "QUIT"
        if e.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if state_screen == 0:                
                if button.pressed(mouse):
                    state_screen = 1   
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    images_hero.draw(screen)
                    pygame.display.flip()
            elif state_screen == 1:
                if card_hero.pressed(mouse):
                    state_screen = 2
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    loc_go.draw(screen)
                    pygame.display.flip()
            elif state_screen == 2:
                if s_go.pressed (mouse):
                    state_screen = 3 
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    heros_ad.draw(screen)
                    pygame.display.flip()
            elif state_screen == 3:
                if h_ad.pressed (mouse):
                    state_screen = 4 
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    loc_go.draw(screen)
                    pygame.display.flip()
            elif state_screen == 4:
                if p_go.pressed (mouse):
                    state_screen = 5 
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    goble_added.draw(screen)
                    pygame.display.flip()
            elif state_screen == 5:
                if h_added.pressed (mouse):
                    state_screen = 6 
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    loc_go.draw(screen)
                    pygame.display.flip()
            elif state_screen == 6:
                if d_go.pressed (mouse):
                    state_screen = 7 
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    yov_ho.draw(screen)
                    pygame.display.flip()
            elif state_screen == 7:
                if v_ho.pressed (mouse):
                    state_screen = 8 
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    duck_map.draw(screen)
                    pygame.display.flip()
            elif state_screen == 8:
                if d_map.pressed (mouse):
                    state_screen = 9 
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    final_arem.draw(screen)
                    pygame.display.flip()
            elif state_screen == 9:
                if f_arem.pressed (mouse):
                    state_screen = 10 
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    knaz_po.draw(screen)
                    pygame.display.flip()
            elif state_screen == 10:
                if kn_po.pressed (mouse):
                    state_screen = 11 
                    screen.fill(white)
                    screen.blit(background_image, (0, 0))
                    konez_vse.draw(screen)
                    pygame.display.flip()
           


