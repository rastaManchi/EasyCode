import pygame
import sys


pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
fps = 120
clock = pygame.time.Clock()


player = pygame.Rect(0, 0, 50, 50)
direction = None


while True:
    screen.fill((100, 100, 100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = 'UP'
            elif event.key == pygame.K_s:
                direction = 'DOWN'
            elif event.key == pygame.K_d:
                direction = 'RIGHT'
            elif event.key == pygame.K_a:
                direction = 'LEFT'
    
    if direction == 'UP':
        player.y -= 2
    elif direction == 'DOWN':
        player.y += 2
    elif direction == 'LEFT':
        player.x -= 2
    elif direction == 'RIGHT':
        player.x += 2
    
    pygame.draw.rect(screen, (0, 255, 0), player)
    
    pygame.display.update()
    clock.tick(fps)



