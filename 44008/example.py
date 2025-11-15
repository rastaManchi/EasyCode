import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(225, 225, 50, 50)
player_img_orig = pygame.image.load('steve.png')
player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))

direction = 'none'

while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                direction = 'right'
            elif e.key == pygame.K_LEFT:
                direction = 'left'
            elif e.key == pygame.K_UP:
                direction = 'up'
            elif e.key == pygame.K_DOWN:
                direction = 'down'
        if e.type == pygame.KEYUP:
            direction = 'none'

    if direction == 'right':
        player.x += 5
    elif direction == 'left':
        player.x -= 5
    elif direction == 'up':
        player.y -= 5
    elif direction == 'down':
        player.y += 5
    
    screen.blit(player_img, player)
    pygame.display.update()
    clock.tick(60)
    
