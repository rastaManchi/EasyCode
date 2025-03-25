import pygame
import random
import sys
import math

pygame.init()

WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

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


    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


    def collide(self, obj):
        return self.rect.colliderect(obj.rect)


    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

walls = []
with open('26847/map.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                walls.append(Wall(col * 20, row * 20, 20, 20, '26847/SANS.png'))
            col += 1
        row += 1


player = Player(30, 30, 50, 50, '26847/steve.png')


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
    
    for wall in walls:
        if player.collide(wall):
            player.rect.x -= player.x_speed
            player.rect.y -= player.y_speed

    for wall in walls:
        wall.draw()

    player.draw()
    
    pygame.display.update()
    clock.tick(60)