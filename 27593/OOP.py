import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


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


player = Player(225, 225, 50, 50, '27593/steve.png', 'none')


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
            if player.rect.x <= x <= player.rect.right and \
                player.rect.y <= y <= player.rect.bottom:
                player.orig_img = pygame.image.load('27593/SANS.png')
                player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                
    
    player.move()
    player.draw()

    pygame.display.update()
    clock.tick(60)