import pygame 
import sys 
from random import *
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
game_state = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Skin:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x,y,w,h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (self.rect.width, self.rect.height))

    def draw(self):
        screen.blit(self.img, self.rect)



class Player:
    def __init__(self, x, y, direction, size,):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.x = 225
        self.y = 225
        self.direction = direction
        self.size = 15
        
    def move(self, dx, dy):
        self.x = dx
        self.y = dy
#хзхз

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
        pygame.draw.circle(screen, (0, 225, 0), (self.x, self.y), self.size)


class Food:
    def __init__(self):
        self.size = 5
        self.x = random.randint(0, 450)
        self.y = random.randint(0, 450)

    def draw(self):
        pygame.draw.circle(screen, (225, 0, 0), (self.x, self.y), self.size)
        

player = Player(225, 225, 'none', 15)
skin1 = Skin(125, 225, 50, 50, 'photo_2025-02-18_16-08-04.jpg' )
skin2 = Skin(250, 225, 50, 50, 'ganius.jpg' )

food_items = [Food() for _ in range(50)]

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
                    player.orig_img = pygame.image.load('ganius.jpg')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                elif skin2.rect.x < x < skin2.rect.right and skin2.rect.y < y < skin2.rect.bottom:
                    player.orig_img = pygame.image.load('photo_2025-02-18_16-08-04.jpg')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
        skin1.draw()
        skin2.draw()
        player.move()
        player.move()

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
                if player.rect.x <= x <= player.rect.right and \
                    player.rect.y <= y <= player.rect.bottom:
                    player.orig_img = pygame.image.load('ganius.jpg')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))

        for food in food_items:
            if (player.x - food.x) ** 2 + (player.y - food.y) ** 2 < (player.size + food.size) ** 2:
                player.size += 1 
                food_items.remove(food)
                food_items.append(Food())
    
        screen.fill((0, 100, 10))
        player.move()
        player.draw()
    for food in food_items:
        food.draw()
    pygame.display.update()
    clock.tick(60)