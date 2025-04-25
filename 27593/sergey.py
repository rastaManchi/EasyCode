import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60

#классы
class Player:
    def __init__(self, x, y, w, h, color, inventory=[]):
        self.rect = pygame.Rect(x, y, w, h)
        # self.orig_img = pygame.image.load(img)
        # self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.color = color
        self.x_speed = 0
        self.y_speed = 2
        self.is_inventory_show = False
        self.inventory = inventory
    
    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
    
    def iscollide(self, obj: pygame.Rect):
        if self.rect.colliderect(obj):
            return True
        return False

    def draw(self):
        # self.frame += 1
        # if self.max_frame < self.frame:
        #     self.frame = 1
        
        # self.orig_img = pygame.image.load(f'41-run-head-{self.frame}.png')
        # self.img = pygame.transform.scale(self.orig_img, (self.rect.width, self.rect.height))
        # screen.blit(self.img, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

class Wall:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))

    def draw(self):
        screen.blit(self.img, self.rect)
        # pygame.draw.rect(screen, (255, 0, 0), self.rect)


lvl1walls = []
file = open('27593/sergey.txt', 'r', encoding='utf-8')
lines = file.read().split('\n')
row = 0
for line in lines:
    items = list(line)
    column = 0
    for x in items:
        if x == '1':
            lvl1walls.append(Wall(column*20, row*20, 20, 20, '27593/wall.jpg'))
        column += 1
    row += 1

#создание экземпляров
player = Player(250, 0, 20, 20, (255, 0, 0))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


while True:
    screen.fill((0, 0 , 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # обработка нажатий
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_speed = -5
            elif event.key == pygame.K_RIGHT:
                player.x_speed = 5
            

    # движение обьектов
    player.move()

    for wall in lvl1walls:
        if player.iscollide(wall):
            player.rect.y -= player.y_speed
        if player.iscollide(wall):
            player.rect.x -= player.x_speed

    #отрисовка объектов
    player.draw()
    for wall in lvl1walls:
        wall.draw()

    pygame.display.update()
    clock.tick(FPS)