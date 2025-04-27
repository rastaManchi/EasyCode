import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60

#классы


#создание экземпляров

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


while True:
    screen.fill(0, 0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # обработка нажатий

    # движение обьектов


    #отрисовка объектов

    pygame.display.update()
    clock.tick(FPS)
