import pygame
import sys

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
    def __init__(self, x, y, w, h, speed, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.speed = speed
        self.speedx = 0
        self.speedy = 0
        
    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
    def collide(self, obj):
        return self.rect.colliderect(obj.rect)
    
    def draw(self):
        screen.blit(self.img, self.rect)

walls = []
with open('map.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                walls.append(Wall(col * 20, row * 20, 20, 20, 'wall.png'))
            col += 1
        row += 1
        
player = Player(25, 25, 20, 20, 5, 'knight.png')

while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                player.speedx = player.speed
            elif e.key == pygame.K_LEFT:
                player.speedx = -player.speed
            elif e.key == pygame.K_UP:
                player.speedy = -player.speed
            elif e.key == pygame.K_DOWN:
                player.speedy = player.speed
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT or e.key == e.key == pygame.K_LEFT:
                player.speedx = 0
            if e.key == pygame.K_UP or e.key == e.key == pygame.K_DOWN:
                player.speedy = 0

    player.move()
    
    for wall in walls:
        if player.collide(wall):
            player.rect.x -= player.speedx
            player.rect.y -= player.speedy

    for wall in walls:
        wall.draw()
        
    player.draw()
    
    pygame.display.update()
    clock.tick(60)