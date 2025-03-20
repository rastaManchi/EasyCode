import pygame 
import sys 
from random import *

pygame.init()

WIDTH = 500
HEIGHT = 500
game_state = ()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Skin:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig.img, (self.rect.width, self.rect.height))

    def draw(self):
        screen.blit(self.img, self.rect)

class Player:
    def __init__(self, x, y , w, h, img, direction):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w ,h))
        self.direction = direction

    def move(self):
        if direction == 'right':
            player.x += 5
        elif direction == 'left':
            player.x -= 5
        elif direction == 'up':
         player.y -= 5
        elif direction == 'down':
            player.y += 5

    def draw(self):
        screen.blit(self.img, self.rect)

class Obstacle:
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

player = Player(225, 225, 50, 50, '27593/steve.png', 'none')
skin1 = Skin("125, 225, 50, 50")
skin2 = Skin("125, 225, 50, 50")

obstacles = [
    Obstacle(150, 150, 100, 10, (255, 0, 0)),  
    Obstacle(300, 300, 10, 100, (0, 255, 0)),  
]

while True:
    screen.fill((255, 255, 255))

    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if player.rect.x <=x <= player.rect.right and skin1.rect.y < y < skin1.rect.bottom:
                    player.orig_img = pygame.image.load('27593/SANS.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                elif player.rect.x <=x <= player.rect.right and skin2.rect.y < y < skin2.rect.bottom:
                    player.orig_img = pygame.image.load('27593/steve.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
        skin1.draw()
        skin2.draw()


    if game_state == 1:


        for obstacle in obstacles:
            obstacle.draw()

    
    player.move()

    if game_state == 1: 

        pygame.display.update()
        clock.tick(60)