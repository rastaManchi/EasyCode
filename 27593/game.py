import pygame


pygame.init()


WIDTH = 500
HEIGHT = 500
FPS = 60
COLOR = (152, 47, 193)
DONIR = (255, 182, 193)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


player = pygame.Rect(0, 0, 50, 50)


direction = 'right'


while True:

    screen.fill(DONIR)

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

    pygame.draw.rect(screen, COLOR, player)

    pygame.display.update()
    clock.tick(FPS)
