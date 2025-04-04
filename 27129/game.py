import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
gamestate = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(img)
        self.transform = pygame.transform.scale(self.image,( self.rect.width, self.rect.height))
        self.x_speed = 0
        self.y_speed = 0

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def iscollide(self, obj):
        if self.rect.colliderect(obj):
            return True
        else:
            return False

    def draw(self):
        screen.blit(self.transform, self.rect)

class Wall:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))

    def draw(self):
        screen.blit(self.img, self.rect)

class Skin:
    def __init__(self, x, y, w, h, img ):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.image.load(img)
        self.transform = pygame.transform.scale(self.image,(self.rect.width, self.rect.height))
    def draw(self):
        screen.blit(self.transform, self.rect)


walls = []
file = open('27129/game.txt', 'r', encoding='utf-8')
lines = file.read().split('\n')
r = 0
for line in lines:
    row = list(line)
    c = 0
    for x in row:
        if x == '1':
            walls.append(Wall(c*20, r*20, 20, 20, '27129/SANS.png'))
        c += 1
    r += 1




skin1 = Skin(125,255, 50,50, '27129/SANS.png')
skin2 = Skin(255,255, 50,50, '27129/steve.png' )
player = Player(255,255, 50,50, '27129/SANS.png')

# player = pygame.Rect(225, 225, 50, 50)
# player_img_orig = pygame.image.load('player.png')
# player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))

# direction = 'none'

while True:
    screen.fill((255, 255, 255))
    if gamestate == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                x,y = e.pos
                if skin1.rect.x < x < skin1.rect.right and skin1.rect.y < y < skin1.rect.bottom:
                    player.image = pygame.image.load('27129/SANS.png')
                    player.transform = pygame.transform.scale(player.image, (player.rect.width, player.rect.height))
                    gamestate = 1
                if skin2.rect.x < x < skin2.rect.right and skin2.rect.y < y < skin2.rect.bottom:
                    player.image = pygame.image.load('27129/steve.png')
                    player.transform = pygame.transform.scale(player.image, (player.rect.width, player.rect.height))
                    gamestate = 1
        skin1.draw()
        skin2.draw()

    if gamestate == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    player.x_speed = 5
                elif e.key == pygame.K_LEFT:
                    player.x_speed = -5
                elif e.key == pygame.K_UP:
                    player.y_speed = -5
                elif e.key == pygame.K_DOWN:
                    player.y_speed = 5
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    player.x_speed = 0
                elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    player.y_speed = 0
            if e.type == pygame.MOUSEBUTTONDOWN:
                print(e.pos)
            
        player.move()

        for wall in walls:
            wall.draw()
        
        for wall in walls:
            if player.iscollide(wall):
                player.rect.x -= player.x_speed
                player.rect.y -= player.y_speed

        player.draw()
    
    pygame.display.update()
    clock.tick(60)