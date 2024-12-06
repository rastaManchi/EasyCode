import pygame

pygame.init()


WIDTH = 500
HEIGHT = 500
FPS = 60
TOMATO = (255, 0, 0)
BG = (100, 100, 100)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
clock = pygame.time.Clock()
player = pygame.Rect(0, 0, 50, 50)
direction = 'right'

while True:
    screen.fill(BG)
    if direction == 'right':
        player.x += 2
        player.y += 2
        if player.x >= 450:
            direction = 'left'
    elif direction == 'left':
        player.x -= 2
        player.y -= 2
        if player.x <= 0:
            direction = 'right'
    pygame.draw.rect(screen, TOMATO, player)
    pygame.display.update()
    
    clock.tick(FPS)

