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
    def __init__(self, x, y, w, h, img, direction):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.direction = direction

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
        screen.blit(player.img, player.rect)

player = Player(0, 0, 200, 200, 'ar.png', 'none')
skin1 = Skin(0, 0, 100, 100, 'po.jpg')
skin2 = Skin(250, 250, 50, 50, 'ar.png')

enemy = pygame.Rect(0, 0, 100, 100)
enemy_orig_im = pygame.image.load('ghf.jpg')
enemy_img = pygame.transform.scale(enemy_orig_im, (enemy.width, enemy.height))

direction = 'none'

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
                    player.orig_img = pygame.image.load('po.jpg')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                elif skin2.rect.x < x < skin2.rect.right and skin2.rect.y < y < skin2.rect.bottom:
                    player.orig_img = pygame.image.load('ar.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1

        skin1.draw()
        skin2.draw()
    if game_state == 1:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_d:
                    player.direction = 'right'
                elif e.key == pygame.K_a:
                    player.direction = 'left'
                elif e.key == pygame.K_w:
                    player.direction = 'up'
                elif e.key == pygame.K_s:
                    player.direction = 'down'
            if e.type == pygame.KEYUP:
                player.direction = 'none'
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if player.rect.x <= x <= player.rect.right and \
                    player.rect.y <= y <= player.rect.bottom:
                    player.orig_img = pygame.image.load('po.jpg')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
            
            if player.rect.colliderect(enemy):
                pay = pygame.Rect(0, 0, 10 , 10)
                pay_orig_img = pygame.image.load('pay.jpg')
                pay_img = pygame.transform.scale(pay_orig_img, (pay.width, pay.height))
                enemy = random
                direction = 'none'

            

        player.move()
        player.draw()
        screen.blit(enemy_img, enemy)
    
    pygame.display.update()
    clock.tick(60)