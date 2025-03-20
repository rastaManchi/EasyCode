import pygame  # подключаем библиотеку
import sys  # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
game_state = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Skin:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (self.rect.width, self.rect.height))

    def draw(self):
        screen.blit(self.img, self.rect)

class Player:
    def __init__(self, x, y, w, h, img, direction):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.direction = direction
    
    def move(self):
        if self.direction == 'right':
            self.rect.x += 5
        elif self.direction == 'left':
            self.rect.x -= 5
        elif self.direction == 'up':
            self.rect.y -= 5
        elif self.direction == 'down':
            self.rect.y += 5 
    
    def draw(self):
        screen.blit(self.img, self.rect)


        
    

player = Player(255, 255,50, 50, 'imposter.png', 'none')
skin1 = Skin(125, 225, 50, 50, "negr.png")
skin2 = Skin(125, 225, 50, 50, "imposter.png" )

class Player_2:
    def two(self,x, y, w, h, img, direction):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.direction = direction
    
    def mor(self):
        if self.direction == 'right':
            self.rect.x += 5
        elif self.direction == 'left':
            self.rect.x -= 5
        elif self.direction == 'up':
            self.rect.y -= 5
        elif self.direction == 'down':
            self.rect.y += 5 
    
    def draws(self):
        screen.blit(self.img, self.rect)
    

player_2 = Player_2(255, 255, 50, 50, 'negr.png', 'none')

while True:
    screen.fill((255, 255, 255))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                player.direction = 'right'
            elif i.key == pygame.K_LEFT:
                player.direction = 'left'
            elif i.key == pygame.K_UP:
                player.direction = 'up'
            elif i.key == pygame.K_DOWN:
                player.direction = 'down'
        if i.type == pygame.KEYUP:
            player.direction = 'none'
        if i.type == pygame.MOUSEBUTTOUNDOWN:
            x, y = i.pos
            if player.rect.x <= x <= player.rect.right and \
                player.rect.y <= y <= player.rect.bottom:
                player.orig_img = pygame.image.load('kop.png')
                player.img = pygame.transform.scale(player.orig_img,(player.rect.width, player.rect.height))
                

while True:
    screen.fill((255, 255, 255))
    if skin1.rect.x == skin2.rect.x and skin1.rect.y == skin2.rect.y:
        skin1.rect.x = 0
        skin1.rect.y = 0   
    
    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if skin1.rect.x < x < skin1.rect.right and skin1.rect.y < y < skin1.rect.bottom:
                    player.orig_img = pygame.image.load('negr.png')  
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                if skin2.rect.x < x < skin2.rect.right and skin2.rect.y < y < skin2.rect.bottom:
                    player.orig_img = pygame.image.load('imposter.png')  
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1     

        skin1.draw()
        skin2.draw()

    if game_state == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    player.direction = 'right'
                elif e.key == pygame.K_LEFT:
                    player.direction = 'left'
                elif e.key == pygame.K_UP:
                    player.direction = 'up'
                elif e.key == pygame.K_DOWN:
                    player.direction = 'down'
            if e.type == pygame.KEYUP:
                player.direction = 'none'
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if player.rect.x <= x <= player.rect.right and \
                    player.rect.y <= y <= player.rect.bottom:
                    player.orig_img = pygame.image.load('lox.png')
                    player.img = pygame.transform.scale(player.orig_img,(player.rect.width, player.rect.height))
                    

        player.move()
        player.draw()
        
    screen.blit(player.img, player.rect)
    pygame.display.update()
    clock.tick(60)
    
    player_2.move()
    player_2.draw()
    
    screen.blit(player_2.img, player_2.rect)
    pygame.display.update()
    clock.tick(60)