import pygame, sys

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)

#классы


#Экземепляры классов



while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # дополнительные условия
    
    #движение обьектов

    #отрисовка обьектов


    pygame.display.update()
    clock.tick(FPS)

