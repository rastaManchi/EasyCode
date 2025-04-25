import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60

font = pygame.font.SysFont('Arial', 15)

#классы
class Button():
    def __init__(self, x, y, w, h, color, text, sobitie):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = font.render(text, True, (0, 0, 0))
        self.sobitie = sobitie

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, (20, self.rect.y + self.rect.height//2 - 7))


#создание экземпляров

buttons = [
    Button(0, 0, 100, 50, (0, 255, 0), 'Привет', 'Hello'),
    Button(0, 60, 100, 50, (0, 255, 0), 'Как дела', 'How are you')
]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # обработка нажатий
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for button in buttons:
                if button.rect.x < x < button.rect.right and button.rect.y < y < button.rect.bottom:
                    if button.sobitie == 'Hello':
                        print('Начался бой!')
                    elif button.sobitie == 'How are you':
                        print('Пощада')


    # движение обьектов


    #отрисовка объектов
    for button in buttons:
         button.draw()

    pygame.display.update()
    clock.tick(FPS)