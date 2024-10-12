import pygame
import sys

pygame.init()
game_state = 0

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BG = (144, 0, 255)

enemy = pygame.Rect(50, 50, 50, 50)
enemy_img_orig = pygame.image.load('player.png')
enemy_img = pygame.transform.scale(enemy_img_orig, (enemy.width, enemy.height))

player = pygame.Rect(250, 250, 50, 50)
player_img_orig = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))
direction = ''

while True:
    if game_state == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 1
        screen.fill(BG)
    if game_state == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = 'up'
                elif event.key == pygame.K_s:
                    direction = 'down'
                elif event.key == pygame.K_a:
                    direction = 'left'
                elif event.key == pygame.K_d:
                    direction = 'right'
                elif event.key == pygame.K_1:
                    player.width = player.width * 2
                    player.height = player.height * 2
                    player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))
                elif event.key == pygame.K_2:
                    player.width = player.width * 0.5
                    player.height = player.height * 0.5
                    player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                    direction = ''
        screen.fill(BG)
        if direction == 'up':
            player.y -= 5
        elif direction == 'down':
            player.y += 5
        elif direction == 'left':
            player.x -= 5
        elif direction == 'right':
            player.x += 5
        if player.colliderect(enemy):
            sys.exit()
        screen.blit(player_img, player)
        screen.blit(enemy_img, enemy)
    pygame.display.update()
    clock.tick(60)