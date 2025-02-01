import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 30

player = pygame.Rect(0, 0, 50, 50)
player_orig_img = pygame.image.load('27278/steve.png')
player_img = pygame.transform.scale(player_orig_img, (player.width, player.height))

COLOR = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

direction_x = None
direction_y = None

while True:

    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.x = 450
                player.y = 450
            if event.key == pygame.K_1:
                COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if event.key == pygame.K_UP:
                direction_y = False
            elif event.key == pygame.K_DOWN:
                direction_y = True
            elif event.key == pygame.K_LEFT:
                direction_x = False
            elif event.key == pygame.K_RIGHT:
                direction_x = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                direction_y = None
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                direction_x = None
    

    if direction_x:
        player.x += 5
    elif not direction_x and direction_x != None:
        player.x -= 5
    if direction_y:
        player.y += 5
    elif not direction_y and direction_y != None:
        player.y -= 5
    
    
    screen.blit(player_img, player)

    pygame.display.update()
    clock.tick(FPS)