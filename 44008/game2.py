import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, w, h, speed, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.direction = 'none'
        
    def move(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
    
    def draw(self):
        screen.blit(self.img, self.rect)

player = Player(100, 100, 50, 50, 10, 'steve.png')

while True:
    screen.fill((255, 255, 255))
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
            print(x, y)
    
    player.move()
    player.draw()
    
    pygame.display.update()
    clock.tick(60)