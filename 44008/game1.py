import pygame
import sys
pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
GRAY = (128, 128, 128)


player = pygame.Rect(0, 0, 50, 50)
direction = 'право'


while True:
    # Задний фон
    screen.fill(GRAY)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.x = 0
                player.y = 0
            if event.key == pygame.K_UP:
                direction = 'верх'
            if event.key == pygame.K_DOWN:
                direction = 'вниз'
            if event.key == pygame.K_LEFT:
                direction = 'лево'
            if event.key == pygame.K_RIGHT:
                direction = 'право'
    # Движение

    # if player.x <= 0:
    #     direction = 'право'
    # elif player.x >= WIDTH - player.width:
    #     direction = 'лево'

    if direction == 'право':
        player.x += 2
    elif direction == 'лево':
        player.x -= 2
    elif direction == 'верх':
        player.y -= 2
    elif direction == 'вниз':
        player.y += 2

    # Отрисовка

    pygame.draw.rect(screen, GREEN, player)

    pygame.display.update()
    clock.tick(FPS)