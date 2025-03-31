import pygame
import random
import sys
import math

pygame.init()

WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

lvl = 1


class Enemy:
    def __init__(self, x, y, w, h, img, p1, p2, direction):
        self.rect =  pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.p1 = p1
        self.p2 = p2
        self.speed = 5
        self.direction = direction

    def move(self):
        if self.p1 > self.p2:
            self.p1, self.p2 = self.p2, self.p1
        if self.direction == 'x':
            self.rect.x += self.speed
            if self.rect.x >= self.p2 or self.rect.x <= self.p1:
                self.speed = -self.speed
        else:
            self.rect.y += self.speed
            if self.rect.y >= self.p2 or self.rect.y <= self.p1:
                self.speed = -self.speed

    def draw(self):
        screen.blit(self.img, self.rect)
            



class Wall:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))


    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))


class Player:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.x_speed = 0
        self.y_speed = 0

    def ischangelvl(self):
        if self.rect.x >= WIDTH:
            self.rect.x = 30
            self.rect.y = 30
            return 2
        elif self.rect.x <= -self.rect.width:
            self.rect.x = 30
            self.rect.y = 30
            return 1
        return False

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


    def collide(self, obj):
        return self.rect.colliderect(obj.rect)


    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

lvl1walls = []
with open('26847/lvl1map.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl1walls.append(Wall(col * 20, row * 20, 20, 20, '26847/SANS.png'))
            col += 1
        row += 1

lvl2walls = []
with open('26847/lvl2map.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl2walls.append(Wall(col * 20, row * 20, 20, 20, '26847/SANS.png'))
            col += 1
        row += 1


player = Player(30, 30, 50, 50, '26847/steve.png')
enemy = Enemy(40, 40, 20, 20, '26847/close_btn.png', 40, 200, 'x')


while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                player.x_speed = -5
            elif e.key == pygame.K_RIGHT:
                player.x_speed = 5
            elif e.key == pygame.K_UP:
                player.y_speed = -5
            elif e.key == pygame.K_DOWN:
                player.y_speed = 5
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                player.x_speed = 0
            elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                player.y_speed = 0

    player.move()
    enemy.move()

    if lvl == 1:
        for wall in lvl1walls:
            if player.collide(wall):
                player.rect.x -= player.x_speed
                player.rect.y -= player.y_speed
        for wall in lvl1walls:
            wall.draw()
    elif lvl == 2:
        for wall in lvl2walls:
            if player.collide(wall):
                player.rect.x -= player.x_speed
                player.rect.y -= player.y_speed
        for wall in lvl2walls:
            wall.draw()

    check_lvl = player.ischangelvl()
    if check_lvl:
        lvl = check_lvl

    player.draw()
    enemy.draw()
    
    pygame.display.update()
    clock.tick(60)