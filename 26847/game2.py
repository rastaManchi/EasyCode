import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player:
    def __init__(self, name, x, y, w, h, img, speed, hp, inventory, skills):
        self.name = name
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.speed = speed
        self.hp = hp
        self.inventory = inventory
        self.skills = skills
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


class Skin:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))

    def draw(self):
        screen.blit(self.img, self.rect)

player = Player('Булат', 0, 0, 50, 52, '26847/steve.png', 5, 100, [], [])

close_btn = pygame.Rect(0, 0, 50, 50)
close_btn_orig_img = pygame.image.load('26847/close_btn.png')
close_btn_img = pygame.transform.scale(close_btn_orig_img, (close_btn.width, close_btn.height))

skin1 = Skin(100, 225, 50, 50, '26847/steve.png')
skin2 = Skin(225, 225, 50, 50, '26847/SANS.png')
skin3 = Skin(350, 225, 50, 50, '26847/close_btn.png')

game_state = 0


while True:
    screen.fill((255, 255, 255))
    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if skin1.rect.x <= x <= skin1.rect.right and skin1.rect.y <= y <= skin1.rect.bottom:
                    player.orig_img = pygame.image.load('26847/steve.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                elif skin2.rect.x <= x <= skin2.rect.right and skin2.rect.y <= y <= skin2.rect.bottom:
                    player.orig_img = pygame.image.load('26847/SANS.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                elif skin3.rect.x <= x <= skin3.rect.right and skin3.rect.y <= y <= skin3.rect.bottom:
                    player.orig_img = pygame.image.load('26847/close_btn.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
        

        skin1.draw()
        skin2.draw()
        skin3.draw()

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
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if player.rect.x < x < player.rect.right and \
                    player.rect.y < y < player.rect.bottom:
                    player.orig_img = pygame.image.load('26847/SANS.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                
                if 0 < x < 50 and 0 < y < 50:
                    sys.exit()

        player.move()

        player.draw()
        screen.blit(close_btn_img, close_btn)

    pygame.display.update()
    clock.tick(60)