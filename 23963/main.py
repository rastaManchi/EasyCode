import pygame
import sys
import random
import time

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


player2 = pygame.Rect(200, 200, 50, 61)
# player_image = pygame.image.load('player.png') # Если изначальный размер картинки нас устраивает
image2 = pygame.image.load('player.png')
player_image2 = pygame.transform.scale(image2, (player2.width, player2.height))

direction2 = ''
start_game = time.time()


game_state = 0
font = pygame.font.SysFont('Arial', 30)
hello_text = font.render('Добро пожаловать!', False, (255, 0, 0))
press_to_start = font.render('Нажмите пробел чтобы начать!', False, (255, 0, 0))


while True:
    screen.fill((255, 255, 255))
    if game_state == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 1
        screen.blit(hello_text, (20, 225))
        screen.blit(press_to_start, (20, 275))
    if game_state == 1:
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

        if player2.height * player2.width > 3050:
            print('Уменьшается')
            start_game = time.time()
            player2.width -= 1
            player2.height -= 1
            player_image2 = pygame.transform.scale(image2, (player2.width, player2.height))

        if player.colliderect(player2):
            if player.width * player.height >= player2.width * player2.height:
                player2.x = random.randint(0, 450)
                player2.y = random.randint(0, 450)
                player2.height = random.randint(61, 150)
                player2.width = random.randint(50, 150)
                player_image2 = pygame.transform.scale(image2, (player2.width, player2.height))
                player.height += 20
                player.width += 20
                player_image = pygame.transform.scale(image, (player.width, player.height))
            else:
                player.x = 0
                player.y = 0
                player.width = 50
                player.height = 61
                player2.width = 50
                player2.height = 61
                player_image = pygame.transform.scale(image, (player.width, player.height))
                player_image2 = pygame.transform.scale(image2, (player2.width, player2.height))

        screen.blit(player_image, player)
        screen.blit(player_image2, player2)

        if player.width >= 500:
            game_state = 2
    if game_state == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.x, player.y, player.width, player.height = 0, 0, 50, 61
                    player2.x, player2.y, player2.width, player2.height = 200, 200, 50, 61
                    player_image = pygame.transform.scale(image, (player.width, player.height))
                    player_image2 = pygame.transform.scale(image2, (player2.width, player2.height))
                    game_state = 1
    pygame.display.update()
    clock.tick(FPS)

