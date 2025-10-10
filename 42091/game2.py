import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


enemy = pygame.Rect(50, 50, 30, 30)
enemy_img = pygame.image.load('ufoRed.png')
enemy_img = pygame.transform.scale(enemy_img, (enemy.width, enemy.height))

font = pygame.font.SysFont('Arial', 30)
start_text_1 = font.render('Добро пожаловать!', False, (255, 0, 0))
start_text_2 = font.render('нажмите на пробел чтобы начать', False, (255, 0, 0))
end_text_1 = font.render('вы прошли игру! нажмите пробел', False, (0, 255, 0))
end_text_2 = font.render('чтобы начать заново', False, (0, 255, 0))
game_state = 0
direction = '0'


class Player:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.direction = None

    def move(self):
        if self.direction == 'left':
            self.rect.x -= 5
        elif self.direction == 'right':
            self.rect.x += 5
        elif self.direction == 'up':
            self.rect.y -= 5
        elif self.direction == 'down':
            self.rect.y += 5

    def draw(self):
        screen.blit(self.img, self.rect)

player = Player(0, 0, 50, 50, "ufoRed.png")


while True:
    screen.fill((255, 255, 255))
    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
        
                    game_state = 1
        screen.blit(start_text_1,(20,225))
        screen.blit(start_text_2,(20,255))
    if game_state == 2:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    player.rect.x, player.rect.y, player.rect.width, player.rect.height = 400, 400, 50, 50
                    enemy.x, enemy.y = 50, 50
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
        screen.blit(end_text_1,(20,225))
        screen.blit(end_text_2,(20,255))
    if game_state == 1:
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

        player.move()

        if player.rect.colliderect(enemy):
            enemy.x = randint(0, 470)
            enemy.y = randint(0, 470)
            player.rect.width += 5
            player.rect.height += 5
            player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))


        if player.rect.width >= 60:
            game_state = 2
        # Здесь весь движ
        player.draw()
        screen.blit(enemy_img, enemy)
    pygame.display.update()
    clock.tick(60)