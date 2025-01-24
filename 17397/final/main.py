import pygame # подключаем библиотеку
import sys # подключаем модуль для 
import time
from random import *

pygame.init()

game_state = 0

font = pygame.font.SysFont('Arial', 30)
start_text = font.render('Начальный текст', False, (255, 255, 255))
end_text = font.render('Финальный текст', False, (255, 255, 255))

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(400, 400, 50, 50)
player_img_orig = pygame.image.load('creeper.png')
player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))

enemy = pygame.Rect(50, 50, 30, 30)
enemy_img = pygame.image.load('knight.png')
enemy_img = pygame.transform.scale(enemy_img, (enemy.width, enemy.height))

direction = 'none'

while True:
    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    game_state = 1
        screen.blit(start_text, (20, 230))
    if game_state == 1:
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
        if direction == 'left':
            player.x -= 5
        if direction == 'up':
            player.y -= 5
        if direction == 'down':
            player.y += 5


        if player.colliderect(enemy):
            enemy.x = randint(0, 470)
            enemy.y = randint(0, 470)
            player.width += 5
            player.height += 5
            player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))

            if player.height >= 200:
                game_state = 2
                player.height = 50
                player.width = 50
                player.x = 100
                player.y = 100
                player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))

        screen.blit(player_img, player)
        screen.blit(enemy_img, enemy)

    if game_state == 2:
        screen.fill((0, 0, 0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    game_state = 1
        screen.blit(end_text, (20, 230))
    pygame.display.update()
    clock.tick(60)