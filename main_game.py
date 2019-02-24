# -*- coding: utf-8 -*-
import pygame
from pygame import *
from mybutton import* 
from houses import * 
from Player import*

yellow    = (255, 255,   0)   
blue      = (  0,   0, 255)    
white     = (255, 255, 255) 

et_mouse  = 'MOUSE'
et_key ='KEY'



class game_text():
    def __init__(self, title, fontname, fontsize, x, y, color1, color2):
        fontObj = pygame.font.Font(fontname, fontsize) # 
        self.textSurfaceObj = fontObj.render(title, True, color1, color2) # сама надпись  
        self.textRectObj = self.textSurfaceObj.get_rect() # 
        self.textRectObj.center = (x, y) # размеры надписи
        self.enable = True

class mysprite(object):
    def __init__(self, name, s, ev_types):
        self.name = name
        self.s = s
        self.ev_types = ev_types
    
    @property
    def sprite(self):
        return self.s

#hero = Player(55,55, "image/anim/hero.png") 
#heros.add(hero)
#left = right = up = down = go = go_back = False 
hero1 = Pistolet(55,55, "image/cards/pistol.jpg")
pistols.add(hero1)
left = right = up = down = go = go_back = False
# экран
class game_screen(object):
    def __init__(self, num, background_file, caption = ""):
        self.number = num
        self.background_image = pygame.image.load(background_file)
        self.sprites = pygame.sprite.Group()
        self.caption = caption
        self.game_texts = []
        self.mysprites = []
        self._key = False
        
    
    def sprite_add(self, s, name: str, event_types):
        msprite = mysprite(name, s, event_types)
        self.sprites.add(s)        
        self.mysprites.append(msprite)
        if 'KEY' in event_types:
            self._key = True
    
    def spritebyname(self, name):
        for s in self.mysprites:
            if s.name == name:
                return s
    
    def text_add(self, game_text):
        self.game_texts.append(game_text)
        
    def check_pressed(self, name, mouse):        
        for i in self.mysprites:
            if i.name == name:               
                return i.sprite.pressed(mouse)    
            
    @property
    def key(self):
        return self._key
    
    def check_key(self, name, left, right, up, down):
        for i in self.mysprites:
            if i.name == name and 'KEY' in i.ev_types:               
                i.sprite.update(left, right, up, down)
                
    def check_pos(self, name1, name2):
        for i in self.mysprites:
            if i.name == name1:
                break
        for j in self.mysprites:
            if j.name == name2:              
                return i.sprite.pos_obj(j.sprite.rect.x, j.sprite.rect.y)
                    
              
        
        
        
# Основной объект с экранами
class root_game(object):
    def __init__(self, WIN_WIDTH, WIN_HEIGHT):
        
        DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # дисплкей по ширине и высоте
        self.screen = pygame.display.set_mode(DISPLAY) #
        
        self._screen_index = -1
        self.screens = []
    
    def get_screen_index(self):
        return self._screen_index
    
    def set_screen_index(self, value):
        if value != self._screen_index:
            if len(self.screens) - 1 >= value:
                self._screen_index = value
                self.update()
            else:
                print('Not screen number ', value, ' len ',len(self.screens) )
            
    def del_screen_index(self):
        self._screen_index = -1
    
    screen_index = property (get_screen_index, set_screen_index, del_screen_index)
    
    @property
    def screen_current(self):
        return self.screens[self._screen_index]

    def screen_add(self, scr):
        self.screens.append(scr)
    
    def update(self):
        scr = self.screens[self.screen_index]
        self.screen.fill(white)
        self.screen.blit(scr.background_image, (0, 0))
        scr.sprites.draw(self.screen)
        for i in scr.game_texts:
            self.screen.blit(i.textSurfaceObj, i.textRectObj)
        pygame.display.update()



def screen_init(rgame: root_game):
    
    # начальный экран
    scr =  game_screen(0, 'image/cards/fon.jpg')
    button = Button('image/cards/button.jpg', 350, 500)
    t = game_text(' Welcome to the game of revenge for the sidekick. Click to button ', 'freesansbold.ttf', 22, 400, 300, yellow, blue)
    scr.sprite_add(button, 'BUTTON0', [et_mouse])
    scr.text_add(t)
    rgame.screen_add (scr)
    
    # 1 экран - начало игры
    scr =  game_screen(1, 'image/cards/card.jpg')
    s = house('image/cards/card2.jpg', 500 , 650)
    scr.sprite_add(s, 'D1', [])       
    s = house ('image/cards/obj.jpg', 200 , 10)
    scr.sprite_add(s, 'D2', [])
    s = house('image/cards/militia.jpg',50,550)
    scr.sprite_add(s, 'D3', [])
    s = house('image/cards/mestovars.jpg',400,400)
    scr.sprite_add(s, 'D4', [])
    s = house('image/cards/dom.jpg',800,100)
    scr.sprite_add(s, 'D5', [])
    s = house ('image/cards/dom2.jpg',750,290)
    scr.sprite_add(s, 'D6', [])
    s = Player(55,55, "image/anim/hero.png") 
    scr.sprite_add(s, 'HERO1', [et_key])
    rgame.screen_add (scr)
    
    # 2 экран ...
    scr =  game_screen(2, 'image/cards/fon2.jpg')
    s = Button('image/cards/text.jpg',250,50)
    scr.sprite_add(s, 'K1', [])    
    s = Button('image/cards/knopka.jpg',100,500)
    scr.sprite_add(s, 'K2', [et_mouse])
    s = Button('image/cards/knopka2.jpg',700,500)
    scr.sprite_add(s, 'K3', [et_mouse])
    rgame.screen_add (scr)
    # 3 экран
    scr =  game_screen(3, 'image/cards/fon2.jpg')
    s = Button('image/cards/text3.jpg',150,50)
    scr.sprite_add(s,'B1',[])
    button = Button('image/cards/button.jpg', 350, 500)
    scr.sprite_add(button, 'BUTTON0', [et_mouse])
    rgame.screen_add (scr)
    # 4 экран
    scr =  game_screen(4, 'image/cards/fon2.jpg')
    s = Button('image/cards/text2.jpg',150,50)
    scr.sprite_add(s,'B2',[])
    rgame.screen_add (scr)
    # 5 экран
    scr =  game_screen(5, 'image/cards/card.jpg')
    s = house('image/cards/card2.jpg', 500 , 650)
    scr.sprite_add(s, 'D1', [])       
    s = house ('image/cards/obj.jpg', 200 , 10)
    scr.sprite_add(s, 'D2', [])
    s = house('image/cards/militia.jpg',50,550)
    scr.sprite_add(s, 'D3', [])
    s = house('image/cards/mestovars.jpg',400,400)
    scr.sprite_add(s, 'D4', [])
    s = house('image/cards/dom.jpg',800,100)
    scr.sprite_add(s, 'D5', [])
    s = house ('image/cards/dom2.jpg',750,290)
    scr.sprite_add(s, 'D6', [])
    s = Player(55,55, "image/anim/hero.png") 
    scr.sprite_add(s, 'HERO1', [et_key])
    rgame.screen_add (scr)
    # 6 экран 
    scr =  game_screen(6, 'image/cards/fon2.jpg')
    s = Button('image/cards/pochta.jpg',150,50)
    scr.sprite_add(s,'B4',[])
    scr.sprite_add(button, 'BUTTON0', [et_mouse])
    rgame.screen_add (scr)

    # экран 7 
    scr =  game_screen(7, 'image/cards/fon2.jpg')
    s = Button('image/cards/pochta1.jpg',150,50)
    scr.sprite_add(s,'B3',[])
    #button = Button('image/cards/button.jpg', 350, 500)
    scr.sprite_add(button, 'BUTTON0', [et_mouse])
    rgame.screen_add (scr)

    #8 экран
    scr =  game_screen(8, 'image/cards/fon2.jpg')
    s = Button('image/cards/text5.jpg',150,50)
    scr.sprite_add(s,'E1',[])
    music = pygame.mixer.music.load('musik/tysa.mp3')
    pygame.mixer.music.play(-1, 0.0)
    scr.sprite_add(button, 'BUTTON0', [et_mouse])
    rgame.screen_add (scr)
    # 9 экран 
    scr =  game_screen(9, 'image/cards/fon2.jpg')
    s = Button('image/cards/kamnata.jpg',150,50)
    scr.sprite_add(s,'E2',[])
    s = Button('image/gopniki/gop3.jpg',300,300)
    scr.sprite_add(s,'E3',[])
    s = Pistolet(55,55, "image/cards/pistols.png") 
    scr.sprite_add(s, 'HERO2', [et_key])
