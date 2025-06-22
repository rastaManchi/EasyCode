import pygame, sys

pygame.init()
HEIGH = 500
WIDTH = 500
FPS = 30

screen = pygame.display.set_mode((WIDTH, HEIGH))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(FPS)