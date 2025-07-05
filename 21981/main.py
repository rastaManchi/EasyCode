import pygame
import sys


WIDTH = 500
HEIGHT = 500
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GRAY = (202, 204, 206)
RED = (255, 0, 0)

pygame.init()

player = pygame.Rect(0, 0, 50, 50)
player_speed = 2

while True:
    screen.fill(GRAY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.x = 100
            
    player.x += player_speed
    if player.x > 450 or player.x < 0:
        player_speed = -player_speed
            
    pygame.draw.rect(screen, RED, player)
            
    pygame.display.update()
    clock.tick(FPS)