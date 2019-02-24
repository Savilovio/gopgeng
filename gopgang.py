# -*- coding: utf-8 -*-
import pygame
from pygame import *
from main_game import root_game, screen_init, game_screen


def main():
    pygame.init()
    rgame = root_game(1000, 800)
    screen_init(rgame)
    rgame.screen_index = 0
    upd = False
    left = right = go = go_back = False 
    
    while True:                
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            
            if e.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if rgame.screen_index == 0:                    
                    if  rgame.screen_current.check_pressed('BUTTON0', mouse):
                        rgame.screen_index = 1
                else:
                    if rgame.screen_index == 2:
                        if rgame.screen_current.check_pressed('K2', mouse):
                            rgame.screen_index = 3
                        else:
                            if rgame.screen_current.check_pressed('K3', mouse):
                                rgame.screen_index = 4
                if rgame.screen_index == 3:                    
                    if  rgame.screen_current.check_pressed('BUTTON0', mouse):
                        left = right = go = go_back = False
                        rgame.screen_index = 5 
                if rgame.screen_index == 6:                    
                    if  rgame.screen_current.check_pressed('BUTTON0', mouse):
                        rgame.screen_index = 7                                                                              
                if rgame.screen_index == 7:                    
                    if  rgame.screen_current.check_pressed('BUTTON0', mouse):
                        left = right = go = go_back = False
                        rgame.screen_index = 8
                if rgame.screen_index == 8:                    
                    if  rgame.screen_current.check_pressed('BUTTON0', mouse):
                        rgame.screen_index = 9  
            
            if  rgame.screen_current.key:
                if e.type == KEYDOWN and e.key == K_LEFT:
                    left = True
                    upd = True
                if e.type == KEYUP and e.key == K_LEFT:
                    left = False
                    upd = True
                if e.type == KEYDOWN and e.key == K_RIGHT:
                    right = True
                    upd = True
                if e.type == KEYUP and e.key == K_RIGHT:
                    right = False
                    upd = True
                if e.type == KEYDOWN and e.key == K_UP:
                    go_back = True
                    upd = True
                if e.type == KEYUP and e.key == K_UP:
                    go_back = False
                    upd = True
                if e.type == KEYDOWN and e.key == K_DOWN:
                    go = True
                    upd = True
                if e.type == KEYUP and e.key == K_DOWN:
                    go = False
                    upd = True            
            
                if upd:
                    upd = False
                    if rgame.screen_index == 1:
                        rgame.screen_current.check_key('HERO1', left, right, go, go_back)                    
                        if  rgame.screen_current.check_pos('D1', 'HERO1'):
                            rgame.screen_index = 2

                        else:
                            rgame.update()
                    if rgame.screen_index == 5:
                        rgame.screen_current.check_key('HERO1', left, right, go, go_back)                    
                        if  rgame.screen_current.check_pos('D5', 'HERO1'):
                            rgame.screen_index = 6
                            pygame.time.wait (5000)
                            rgame.screen_index = 7
                        else:
                            rgame.update()
                    if rgame.screen_index == 9:
                        rgame.screen_current.check_key('HERO2', left, right, go, go_back)                    
                        if  rgame.screen_current.check_pos('E3', 'HERO2'):
                            rgame.screen_index = 10
                        else:
                            rgame.update()

# Запуск главной функции
if __name__ == "__main__":
    main()