import pygame
from pygame import *
print("Welcome to Witmario")

from Player import Player # игрока перетаскиваем в основу 
from blocks import Platform

# Главная функция программы
def main():
    pygame.init() 
    # Инициализация начальных значений
    WIN_WIDTH = 800
    WIN_HEIGHT = 640
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
    BACKGROUND_COLOR = "#004400"
    HERO_COLOR = "#FF6262" #"#440043"
    background_image = pygame.image.load('images/background.jpg')
    block_image = image.load("images/blocks.jpg")
    x=y=0
    timer = pygame.time.Clock()
    timer.tick(60) # время 
    PLATFORM_WIDTH =  32
    PLATFORM_HEIGHT = 32
    PLATFORM_COLOR = "#FF6262" # цвет платформы 
    level = [
            "-------------------------",
            "-                  -    -",
            "-                       -",
            "-                       -",
            "-             -----     -",
            "-                       -",
            "---          -          -",
            "-          -            -",
            "-              -------- -",
            "-                       -",
            "-            ---------- -",
            "-    -----              -",
            "--                      -",
            "-   -----------         -",
            "--                     --",
            "-              ---      -",
            "-                   --- -",
            "-                      --",
            "-                  ------",
            "-------------------------"]

 # настраиваем лвл 
    pygame.display.set_caption("Witmario")
    bg = Surface((WIN_WIDTH, WIN_HEIGHT)) 
    entities = pygame.sprite.Group()
    platforms = []
    music = pygame.mixer.music.load('muzik/Lazare.mp3')
    pygame.mixer.music.play(-1, 0.0)
    screen = pygame.display.set_mode(DISPLAY)
# задаём героя 
    hero = Player(55,55) 
    entities.add(hero)
    left = right = False 
    up = False
    # Цикл бесконечного ожидания событий (клавиш, мышки, ...)
    while 1:        
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        
        screen.blit(background_image, (0, 0))
        #screen.blit(bg, (0,0))
        x=y=0
        for row in level:  # вся строка 
            x=0   # на каждой новой строчке x обнуляется     
            for col in row: # каждый символ  
                if col == "-":
                    # создание блока и заливка цветом 
                    if col == "-":
                        pf = Platform(x,y)
                        entities.add(pf)
                        platforms.append(pf)
                      
                x += PLATFORM_WIDTH # установка блоков плотформы  по ширине блоков 
            y += PLATFORM_HEIGHT    # установка блоков плотформы  по высоте  блоков 

        hero.update(left, right, up, platforms)
        entities.draw(screen)
        pygame.display.update()

        

        
# Запуск главной функции
if __name__ == "__main__":
    main()
 