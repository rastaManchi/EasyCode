import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60

#классы
class Ball:
    def __init__(self, x, y, w, h, color, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.x_speed = speed
        self.y_speed = speed

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
    
    def check_win(self):
        pass

    def check_lose(self):
        pass

    def iscollidewalls(self):
        if self.rect.y >= HEIGHT or self.rect.y <= 0:
            self.y_speed = -self.y_speed
        if self.rect.x >= WIDTH or self.rect.x <= 0:
            self.x_speed = - self.x_speed

    def draw(self):
        pygame.draw.ellipse(screen, self.color, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect)


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
