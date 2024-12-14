import pygame
import sys
import random

pygame.init()


WIDTH = 500
HEIGHT = 500
FPS = 60
TOMATO = (255, 0, 0)
BG = (100, 100, 100)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
clock = pygame.time.Clock()

player = pygame.Rect(0, 0, 50, 61)
# player_image = pygame.image.load('player.png') # Если изначальный размер картинки нас устраивает
image = pygame.image.load('player.png')
player_image = pygame.transform.scale(image, (player.width, player.height))

direction = ''


player2 = pygame.Rect(0, 0, 50, 61)
# player_image = pygame.image.load('player.png') # Если изначальный размер картинки нас устраивает
image2 = pygame.image.load('player.png')
player_image2 = pygame.transform.scale(image2, (player2.width, player2.height))

direction2 = ''

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            if event.key == pygame.K_w:
                direction2 = 'up'
            elif event.key == pygame.K_s:
                direction2 = 'down'
            elif event.key == pygame.K_d:
                direction2 = 'right'
            elif event.key == pygame.K_a:
                direction2 = 'left'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or \
                        event.key == pygame.K_DOWN or \
                        event.key == pygame.K_RIGHT or \
                        event.key == pygame.K_LEFT:
                direction = ''
            if event.key == pygame.K_w or \
                        event.key == pygame.K_s or \
                        event.key == pygame.K_d or \
                        event.key == pygame.K_a:
                direction2 = ''

    screen.fill(BG)
    if direction == 'up':
        player.y -= 5
    elif direction == 'down':
        player.y += 5
    elif direction == 'right':
        player.x += 5
    elif direction == 'left':
        player.x -= 5

    if direction2 == 'up':
        player2.y -= 5
    elif direction2 == 'down':
        player2.y += 5
    elif direction2 == 'right':
        player2.x += 5
    elif direction2 == 'left':
        player2.x -= 5
    # pygame.draw.rect(screen, TOMATO, player) Квадрат вместо игрока
    screen.blit(player_image, player)
    screen.blit(player_image2, player2)
    pygame.display.update()
    
    clock.tick(FPS)

