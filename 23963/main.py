import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
clock = pygame.time.Clock()


class Sprite:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.direction = 'none'

    def move(self):
        if self.direction == 'right':
            self.rect.x += 5
        elif self.direction == 'left':
            self.rect.x -= 5
        elif self.direction == 'up':
            self.rect.y -= 5
        elif self.direction == 'down':
            self.rect.y += 5

    def draw(self):
        screen.blit(self.img, self.rect)

player = Sprite(225, 225, 50, 50, 'steve.png')
enemy = Sprite(50, 50, 30, 30, 'SANS.png')
button = Sprite(0, 0, 50, 50, 'close_btn.png')

game_state = 0

font = pygame.font.SysFont('Arial', 30)
start_text = font.render('Нажми на пробел!', False, (255, 0, 0))
end_text = font.render('Игра окончена', False, (0, 255, 0))
restart_text_1 = font.render('Пробел, чтобы', False, (100, 150, 0))
restart_text_2 = font.render('перезапустить игру!', False, (100, 150, 0))

 

while True:
    screen.fill((0, 0, 0))
    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    game_state = 1
        screen.blit(start_text, (20, 255))
    elif game_state == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    player.direction = 'right'
                elif e.key == pygame.K_LEFT:
                    player.direction = 'left'
                elif e.key == pygame.K_UP:
                    player.direction = 'up'
                elif e.key == pygame.K_DOWN:
                    player.direction = 'down'
            if e.type == pygame.KEYUP:
                player.direction = 'none'
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if 0 < x < 50 and 0 < y < 50:
                    sys.exit()

        player.move()

        if player.rect.colliderect(enemy.rect):
            enemy.rect.x = randint(0, 470)
            enemy.rect.y = randint(0, 470)
            player.rect.width += 100
            player.rect.height += 100
            player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))

        if player.rect.width >= 500:
            game_state = 2

        player.draw()
        enemy.draw()
        button.draw()
    elif game_state == 2:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    player.rect.x = 255
                    player.rect.y = 255
                    player.rect.width = 50
                    player.rect.height = 50
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    enemy.rect.x = 50
                    enemy.rect.y = 50
                    game_state = 1
        screen.blit(end_text, (20, 255))
        screen.blit(restart_text_1, (20, 300))
        screen.blit(restart_text_2, (20, 345))

    pygame.display.update()
    clock.tick(60)