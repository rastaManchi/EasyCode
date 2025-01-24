import pygame
pygame.init()


WIDTH = 500
HEIGHT = 500
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


player = pygame.Rect(0, 0, 50, 50)
direction = 'right'

while True:
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    if direction == 'right':
        if player.x <= 450:
            player.x += 2
            player.y += 2
        else:
            direction = 'left'
    else:
        if player.x >= 0:
            player.x -= 2
            player.y -= 2
        else:
            direction = 'right'
    pygame.display.update()
    clock.tick(FPS)

