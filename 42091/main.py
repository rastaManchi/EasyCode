import pygame
import os
import sys


pygame.init()
WIDTH = 500
HEIGHT = 500 
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Wall:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x,y,w,h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        
    def draw(self):
        screen.blit(self.img, self.rect)


lvl_map = []


if os.path.exists("lvl1.txt"):
    file = open('lvl1.txt', 'r')
    stroki = file.read().split('\n')
    row = 0
    for stroka in stroki:
        symbols = list(stroka)
        col = 0
        for symbol in symbols:
            if symbol == "1":
                wall = Wall(20*col, 20*row, 20, 20, "wall.webp")
                lvl_map.append(wall)
            col += 1
        row += 1



while True:
    
    screen.fill((125, 125, 125))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    for wall in lvl_map:
        wall.draw()
        
        
    pygame.display.update()
    clock.tick(FPS)