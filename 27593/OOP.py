import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
game_state = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



class Skin:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (self.rect.width, self.rect.height))

    def draw(self):
        screen.blit(self.img, self.rect)

class Player:
    def __init__(self, x, y, w, h, img, direction, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.direction = direction
        self.speed = speed

    def move(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

    def draw(self):
        screen.blit(self.img, self.rect)


player = Player(225, 225, 50, 50, '27593/steve.png', 'none', 5)
skin1 = Skin(125, 225, 50, 50, '27593/SANS.png')
skin2 = Skin(250, 225, 50, 50, '27593/steve.png')


while True:
    screen.fill((255, 255, 255))

    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if skin1.rect.x < x < skin1.rect.right and skin1.rect.y < y < skin1.rect.bottom:
                    player.orig_img = pygame.image.load('27593/SANS.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                elif skin2.rect.x < x < skin2.rect.right and skin2.rect.y < y < skin2.rect.bottom:
                    player.orig_img = pygame.image.load('27593/steve.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
        skin1.draw()
        skin2.draw()

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
                elif e.key == pygame.K_LSHIFT:
                    a = input('Быстрее?')
                    if a == 'Да':
                        player.speed *= 2
            if e.type == pygame.KEYUP:
                player.direction = 'none'
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if player.rect.x <= x <= player.rect.right and \
                    player.rect.y <= y <= player.rect.bottom:
                    player.orig_img = pygame.image.load('27593/SANS.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    
        
        player.move()
        player.draw()

    pygame.display.update()
    clock.tick(60)