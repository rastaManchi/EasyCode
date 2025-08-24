import pygame
import sys
import os
from random import randint

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

click = pygame.Rect(225, 225, 50, 50)
score = 0
seconds_left = 10
iterations = 0

font = pygame.font.SysFont('Arial', 20)
left_seconds_text = font.render(str(seconds_left), False, (255, 0, 0))
score_text = font.render(str(score), False, (255, 0, 0))

nickname = input('Введите ваш никнейм: ').lower()
prev_record = -1
if os.path.exists(f'{nickname}.txt'):
    file = open(f'{nickname}.txt', 'r')
    prev_record = file.read()
    file.close()

record_text = font.render(f'Прошлый рекорд: {prev_record}', False, (255, 0, 0))


while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if click.collidepoint(e.pos[0], e.pos[1]):
                score += 1
                score_text = font.render(str(score), False, (255, 0, 0))
                click.x = randint(0, 450)
                click.y = randint(0, 450)


    pygame.draw.rect(screen, (0, 0, 0), click)
    screen.blit(left_seconds_text, (10, 10))
    screen.blit(score_text, (480, 10))
    if prev_record != -1:
        screen.blit(record_text, (10, 480))

    iterations += 1
    if iterations == 60:
        seconds_left -= 1
        iterations = 0
        left_seconds_text = font.render(str(seconds_left), False, (255, 0, 0))

    if seconds_left == -1:
        file = open(f'{nickname}.txt', 'w')
        file.write(str(score))
        file.close()
        sys.exit()

    pygame.display.update()
    clock.tick(60)