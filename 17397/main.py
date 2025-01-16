import pygame
import sys
import random

pygame.init()
WIDTH = 1920
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

black = (0, 0, 0)

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


    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.x += self.x_speed


        self.rect.y += self.y_speed



    def collide(self, obj):
        return self.rect.colliderect(obj.rect)

lvl1walls = []
with open('main.txt','r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl1walls.append(Wall(col * 40, row * 40, 40, 40, 'wall.png'))
            col += 1
        row += 1
player = Player(80 ,80, 40, 40,'wall.png')
def roll():
    random_character = random.randint(1,3)
    file_name = f"character{random_character}.png"
    player.img = pygame.transform.scale(pygame.image.load(file_name), (player.rect.width, player.rect.height))
while True:
    screen.fill(black)
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
            elif e.key == pygame.K_SPACE:
                roll()
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                player.x_speed = 0
            elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                player.y_speed = 0
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
        if e.type == pygame.MOUSEMOTION:
            print(e.pos)
    for wall in lvl1walls:
                wall.draw()
    player.move()
    player.draw()
    pygame.display.update()
    clock.tick(60)