import pygame, sys


HEIGHT = 500
WIDTH = 500
FPS = 60
BACKGROUND = (150, 209, 227)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(0, 0, 50, 50)
speed = 2

while True:
    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

    player.x += speed
    if player.x >= 450 or player.x <= 0:
        speed = -speed
    pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.update()
    clock.tick(FPS)