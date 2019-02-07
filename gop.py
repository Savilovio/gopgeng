
# -*- coding: utf-8 -*-
from mybutton import* 
from pygame import *
from houses import * 
from Player import*
import time 
import configparser

yellow    = (255, 255,   0)   
blue      = (  0,   0, 255)    
white     = (255, 255, 255) 

def main():
    pygame.init()
    background_image = pygame.image.load('image/cards/fon.jpg') # путь до картинки 
    WIN_WIDTH = 1000 #размеры
    WIN_HEIGHT = 800 #экрана
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # дисплкей по ширине и высоте 
    screen = pygame.display.set_mode(DISPLAY) # 
    screen.blit(background_image, (0, 0)) # 
    entities = pygame.sprite.Group()
    heros = pygame.sprite.Group()
    doms = pygame.sprite.Group()
    kpki  = pygame.sprite.Group()
    ekran4 = pygame.sprite.Group()
    pianka = pygame.sprite.Group()
    texts = pygame.sprite.Group()
    mentovka = pygame.sprite.Group()
    mios = pygame.sprite.Group()
    bandit = pygame.sprite.Group()
    pistols = pygame.sprite.Group()
    temza = pygame.sprite.Group() 
    tats =  pygame.sprite.Group()
    k = pygame.sprite.Group()
    mmm = pygame.sprite.Group()
    dead = pygame.sprite.Group()
    pygame.display.set_caption('revenge for the sidekick')
    pygame.display.update()#обновляем экран
# создаём надпись
    fontObj = pygame.font.Font('freesansbold.ttf', 22) # 
    textSurfaceObj = fontObj.render(' Welcome to the game of revenge for the sidekick. Click to button ', True, yellow, blue) # сама надпись  
    textRectObj = textSurfaceObj.get_rect() # 
    textRectObj.center = (400, 300) # размеры надписи

    screen.blit(textSurfaceObj, textRectObj)
    button = Button('image/cards/button.jpg', 350, 500)
    entities.add(button)  
    entities.draw(screen)
    #music = pygame.mixer.music.load('musik/bitva.mp3')
    #pygame.mixer.music.play(-1, 0.0)
    pygame.display.update()
    
    background_image = pygame.image.load('image/cards/card.jpg')

    # задаём героя 
    
    hero = Player(55,55, "image/anim/hero.png") 
    heros.add(hero)
    left = right = up = down = go = go_back = False 

    hero1 = Pistolet(55,55, "image/cards/pistol.jpg")
    pistols.add(hero1)
    left = right = up = down = go = go_back = False 


    d_doms = house('image/cards/card2.jpg', 500 , 650)
    ob_doms = house ('image/cards/obj.jpg', 200 , 10)
    m_doms = house('image/cards/militia.jpg',50,550)
    mest_doms = house('image/cards/mestovars.jpg',400,400)
    ddd_doms = house('image/cards/dom.jpg',800,100)
    g_doms = house ('image/cards/dom2.jpg',750,290)
    doms.add(g_doms)
    doms.add(d_doms)  
    doms.add(ob_doms)
    doms.add(m_doms)
    doms.add(mest_doms)
    doms.add(ddd_doms)
    k0_kpki = Button('image/cards/text.jpg',250,50)
    k1_kpki = Button('image/cards/knopka.jpg',100,500)
    k2_kpki = Button('image/cards/knopka2.jpg',700,500)
    kpki.add(k0_kpki)
    kpki.add(k1_kpki)  
    kpki.add(k2_kpki) 
    e1_ekran4 = Button ('image/cards/text2.jpg',50,50)
    ekran4.add(e1_ekran4)
    p1_pianka = Button ('image/cards/text3.jpg',50,50)
    pianka.add(p1_pianka)
    t1_texts = Button ('image/cards/text5.jpg',50,50)
    texts.add(t1_texts)
    m1_mentovka = Button ('image/cards/text4.jpg',50,50)
    mentovka.add(m1_mentovka)
    m1_mios = Button ('image/cards/komnata.jpg',50,50)
    b1_bandit = Button ('image/gopniki/gop3.jpg',300,300)
    t1_temza = Button ('image/gopniki/gop1.jpg',300,50)
    t1_tats = Button ('image/cards/nagr.jpg',300,100)
    k1_k = Button ('image/cards/knopka3.jpg',100,300)
    k2_k =  Button ('image/cards/knopka4.jpg',600,300)
    m1_mmm = Button ('image/cards/militia2.jpg',50,50)
    d1_dead = Button ('image/cards/eslinazk4.jpg',400,200)

    bandit.add(b1_bandit)
    mios.add(m1_mios)
    temza.add(t1_temza)
    tats.add(t1_tats)
    k.add(k1_k)
    k.add(k2_k)
    mmm.add(m1_mmm)
    dead.add(d1_dead)
    pygame.display.update()
    state_screen = 0
    config = configparser.ConfigParser()
    config.read('setting.ini')
    deb = config['debug']
    state_screen = int(deb['state_screen'])


    while state_screen < 15:        
        upd_flag = False
        for e in pygame.event.get():
            if e.type == QUIT:
                #raise SystemExit, "QUIT"d
                state_screen = 16           
            if e.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if state_screen == 0:                
                    if button.pressed(mouse):
                        state_screen = 1
                else:
                    if state_screen == 2:
                        if k1_kpki.pressed(mouse):
                            state_screen = 3
                        if k2_kpki.pressed(mouse):
                            state_screen = 4 
                    else: 
                        if state_screen == 3:                
                            if button.pressed(mouse):
                                state_screen = 5
                        else: 
                            if state_screen == 6:
                                if button.pressed(mouse):
                                    state_screen = 7
                            else:                   
                                if state_screen == 7:
                                    if button.pressed(mouse):
                                        state_screen = 8
                                else: 
                                    if state_screen == 10:
                                        if k1_k.pressed(mouse):
                                            state_screen = 11
                                    else:
                                        if state_screen == 10:
                                            if k2_k.pressed(mouse):
                                                state_screen = 12
                
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
                upd_flag = True
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
                upd_flag = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
                upd_flag = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
                upd_flag = True
            if e.type == KEYDOWN and e.key == K_UP:
                go_back = True
                upd_flag = True
            if e.type == KEYUP and e.key == K_UP:
                go_back = False
                upd_flag = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                go = True
                upd_flag = True
            if e.type == KEYUP and e.key == K_DOWN:
                go = False
                upd_flag = True

            if state_screen == 1:
                screen.blit(background_image, (0, 0))
                hero.update(left, right, go, go_back)
                doms.draw(screen)
                heros.draw(screen)    
                pygame.display.update()

            if state_screen == 1:
            #for h in houses 
                if d_doms.pos_obj(hero.rect.x, hero.rect.y):
                    state_screen = 2

            if state_screen == 2: 
                screen.fill(white)
                kpki.draw(screen)
                pygame.display.flip()

            if state_screen == 3: 
                screen.fill(white)
                pianka.draw(screen)
                entities.draw(screen)
                pygame.display.flip()
            
            if state_screen == 4: 
                screen.fill(white)
                ekran4.draw(screen)
                pygame.display.flip()
            
            if state_screen == 5:
                screen.blit(background_image, (0, 0))
                hero.update(left, right, go, go_back)
                doms.draw(screen)
                heros.draw(screen)    
                pygame.display.update()
            
            if state_screen == 5:
                if ddd_doms.pos_obj(hero.rect.x, hero.rect.y):
                    state_screen = 6

            if state_screen == 6:
                screen.fill(white)
                texts.draw(screen)
                entities.draw(screen)
                #music = pygame.mixer.music.load('musik/tysa.mp3')
                #pygame.mixer.music.play(-1, 0.0)
                pygame.display.update()

            if state_screen == 7:
                screen.fill(white)
                mentovka.draw(screen)
                entities.draw(screen)
                pygame.display.update()

            if state_screen == 8:
                screen.blit(background_image, (0, 0))
                hero.update(left, right, go, go_back)
                doms.draw(screen)
                heros.draw(screen)    
                pygame.display.update()
            
            if state_screen == 8:
                if g_doms.pos_obj(hero.rect.x, hero.rect.y):
                    state_screen = 9
                    screen.fill(white)
                    hero1.update(left, right, go, go_back)
                    mios.draw(screen)
                    bandit.draw(screen)
                    pistols.draw(screen)
                    pygame.display.update()

            
            #if state_screen == 9:
            #    screen.fill(white)
            #    hero1.update(left, right, go, go_back)
            #    mios.draw(screen)
            #    bandit.draw(screen)
            #    pistols.draw(screen)
            #    pygame.display.update()

            if state_screen == 9:
                if b1_bandit.pos_obj(hero1.rect.x, hero1.rect.y):
                    #if b1_bandit.pressed(mouse):
                    screen.blit(background_image, (0, 0))
                    screen.fill(white)
                    mios.draw(screen)
                    temza.draw(screen)
                    pygame.display.update()    
                    print("start sleep")
                    time.sleep(1)
                    print ("end sleep")
                    screen.blit(background_image,(0,0))
                    tats.draw(screen)
                    k.draw(screen)
                    pygame.display.update
                    state_screen = 10
                    print("screen 10")
                else:
                    state_screen = 9

            if state_screen == 10:
                print ("screen 10 paint")
                screen.blit(background_image,(0,0))
                screen.fill(white)
                mmm.draw(screen)
                entities.draw(screen)
                pygame.display.update
            
            if state_screen == 11:
                screen.blit(background_image,(0,0))
                screen.fill(white)
                dead.draw(screen)
                pygame.display.update




# Запуск главной функции
if __name__ == "__main__":
    main()