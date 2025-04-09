import pygame  # подключаем библиотеку
import sys  # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
game_state = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Wall:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))

    def draw(self):
        screen.blit(self.img, self.rect)
        # pygame.draw.rect(screen, (255, 0, 0), self.rect)


class Skin:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (self.rect.width, self.rect.height))

    def draw(self):
        screen.blit(self.img, self.rect)

class Enemy:
    def __init__(self, x, y, w, h, color, img, p1, p2, orientation):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        if p1 > p2:
            p1, p2 = p2, p1
        self.p1 = p1
        self.p2 = p2
        self.orientation = orientation
        self.speed = 5

    def draw_with_img(self):
        screen.blit(self.img, self.rect)

    def draw_without_img(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        if self.orientation == 'x':
            if self.p1 > self.rect.x or self.p2 < self.rect.x:
                self.speed = -self.speed
            self.rect.x += self.speed
        elif self.orientation == 'y':
            if self.p1 > self.rect.y or self.p2 < self.rect.x:
                self.speed = -self.speed
            self.rect.y += self.speed


class Player:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.x_speed = 0
        self.y_speed = 0
    
    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
    
    def iscollide(self, obj: pygame.Rect):
        if self.rect.colliderect(obj):
            return True
        return False

    def draw(self):
        screen.blit(self.img, self.rect)


walls = []
file = open('27593/game3.txt', 'r', encoding='utf-8')
lines = file.read().split('\n')
row = 0
for line in lines:
    items = list(line)
    column = 0
    for x in items:
        if x == '1':
            walls.append(Wall(column*20, row*20, 20, 20, '27593/SANS.png'))
        column += 1
    row += 1

    

player = Player(40, 40,50, 50, '27593/steve.png')
skin1 = Skin(125, 225, 50, 50, "27593/steve.png")
skin2 = Skin(250, 225, 50, 50, "27593/SANS.png" )
enemy = Enemy(100, 100, 50, 50, (255, 0, 0), '27593/steve.png', 100, 300, 'x')

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
                    player.orig_img = pygame.image.load('27593/steve.png')  
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                if skin2.rect.x < x < skin2.rect.right and skin2.rect.y < y < skin2.rect.bottom:
                    player.orig_img = pygame.image.load('27593/SANS.png')  
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1     

        skin1.draw()
        skin2.draw()

    if game_state == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    player.x_speed = -5
                elif e.key == pygame.K_RIGHT:
                    player.x_speed = 5
                if e.key == pygame.K_UP:
                    player.y_speed = -5
                elif e.key == pygame.K_DOWN:
                    player.y_speed = 5
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    player.x_speed = 0
                if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    player.y_speed = 0

        player.move()

        enemy.move()

        for wall in walls:
            wall.draw()

        for wall in walls:
            if player.iscollide(wall):
                player.rect.x -= player.x_speed
                player.rect.y -= player.y_speed
        enemy.draw_with_img()
        player.draw()

    pygame.display.update()
    clock.tick(60)
    