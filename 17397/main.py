import pygame
import random
import sys
import math

pygame.init()

WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

walls = []
with open('map.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                walls.append(pygame.Rect(col * 20, row * 20, 20, 20))
                print(row, col)
            col += 1
        row += 1

BLACK = (0, 0, 0)
RED = (255, 0, 0)
print('done')
    



while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()


    for wall in walls:
        pygame.draw.rect(screen, RED, wall)
    
    pygame.display.update()
    clock.tick(60)