import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 30

player = pygame.Rect(0, 0, 50, 50)
player_orig_img = pygame.image.load('27278/SANS.png')
player_img = pygame.transform.scale(player_orig_img, (player.width, player.height))

food = pygame.Rect(480, 480, 20, 20)

enemy = pygame.Rect(100, 100, 200, 200)
enemy_orig_img = pygame.image.load('27278/steve.png')
enemy_img = pygame.transform.scale(enemy_orig_img, (enemy.width, enemy.height))

COLOR = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

direction_x = None
direction_y = None

direction2_x = None
direction2_y = None

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

            if event.key == pygame.K_w:
                direction2_y = False
            elif event.key == pygame.K_s:
                direction2_y = True
            elif event.key == pygame.K_a:
                direction2_x = False
            elif event.key == pygame.K_d:
                direction2_x = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                direction_y = None
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                direction_x = None

            if event.key == pygame.K_w or event.key == pygame.K_s:
                direction2_y = None
            if event.key == pygame.K_a or event.key == pygame.K_d:
                direction2_x = None
    

    if direction_x:
        player.x += 5
    elif not direction_x and direction_x != None:
        player.x -= 5
    if direction_y:
        player.y += 5
    elif not direction_y and direction_y != None:
        player.y -= 5

    if direction2_x:
        enemy.x += 5
    elif not direction2_x and direction2_x != None:
        enemy.x -= 5
    if direction2_y:
        enemy.y += 5
    elif not direction2_y and direction2_y != None:
        enemy.y -= 5

    if player.colliderect(enemy):
        if player.width >= enemy.width:
            enemy.x = random.randint(0, 450)
            enemy.y = random.randint(0, 450)
            player.width += 20
            player.height += 20
            player_img = pygame.transform.scale(player_orig_img, (player.width, player.height))

    if player.colliderect(food):
        food.x = random.randint(0, 480)
        food.y = random.randint(0, 480)
        player.width += 10
        player.height += 10
        player_img = pygame.transform.scale(player_orig_img, (player.width, player.height))
    
    
    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)
    pygame.draw.rect(screen, COLOR, food)

    pygame.display.update()
    clock.tick(FPS)