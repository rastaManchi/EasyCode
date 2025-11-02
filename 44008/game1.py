import pygame
import sys
import random
pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)


player = pygame.Rect(0, 0, 50, 50)
enemy = pygame.Rect(100, 100, 50, 50)
direction = 'право'


font = pygame.font.SysFont("Arial", 25)
start_text = font.render("Нажмите Пробел, чтобы начать!", True, GREEN)


game_state = 0


while True:
    
    if game_state == 0:
        screen.fill(GRAY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 1
        screen.blit(start_text, (50, 50))
    elif game_state == 1:
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

        if direction == 'право':
            player.x += 2
        elif direction == 'лево':
            player.x -= 2
        elif direction == 'верх':
            player.y -= 2
        elif direction == 'вниз':
            player.y += 2

        if player.colliderect(enemy):
            enemy.x = random.randint(0, 450)
            enemy.y = random.randint(0, 450)
            player.width += 5
            player.height += 5

        # Отрисовка

        pygame.draw.rect(screen, GREEN, player)
        pygame.draw.rect(screen, RED, enemy)
    elif game_state == 2:
        pass
    
    pygame.display.update()
    clock.tick(FPS)