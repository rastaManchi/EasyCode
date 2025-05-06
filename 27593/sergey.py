import pygame
import sys
import random
import time

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60
game_state = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
lvl = 1

#классы

class Wall:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))

    def draw(self):

        screen.blit(self.img, self.rect)
        # pygame.draw.rect(screen, (255, 0, 0), self.rect)


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
            if self.p1 > self.rect.y or self.p2 < self.rect.y:
                self.speed = -self.speed
            self.rect.y += self.speed


class Skin:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (self.rect.width, self.rect.height))

    def draw(self):
        screen.blit(self.img, self.rect)

class Player:
    def __init__(self, x, y, w, h, img, inventory=[]):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.x_speed = 0
        self.y_speed = 2
        self.is_inventory_show = False
        self.inventory = inventory
        self.jump_time = 0
        self.is_jump = True
        
    
    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
   

    def iscollide(self, obj: pygame.Rect):
        if self.rect.colliderect(obj):
            return True
        return False
    

    def draw(self):
        screen.blit(self.img, self.rect)

        
class Wall:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))

    def draw(self):

        screen.blit(self.img, self.rect)

lvl1walls = []
file = open('karta.txt', 'r', encoding='utf-8')
lines = file.read().split('\n')
row = 0
for line in lines:
    items = list(line)
    column = 0
    for x in items:
        if x == '1':
            lvl1walls.append(Wall(column*20, row*20, 20, 20, 'trava.png'))
        if x == '2':
            lvl1walls.append(Wall(column*20, row*20, 20, 20, 'zemlia.png'))
        column += 1
    row += 1

jump = False

#создание экземпляров
player = Player(40, 40, 50, 50, 'gg.png')
skin1 = Skin(100, 100, 400, 300, "ava.png")
skin2 = Skin(205, 300, 300, 300, "start.png" )

bg = pygame.Rect(0, 0, WIDTH, HEIGHT)
bg_orig_pic = pygame.image.load('steve.png')
bg_pic = pygame.transform.scale(bg_orig_pic, (WIDTH, HEIGHT))

enemies = [
    Enemy(100, 100, 50, 50, (255, 0, 0), 'vrag.png', 100, 300, 'x'),
    Enemy(200, 200, 50, 50, (255, 0, 0), 'vrag.png', 200, 400, 'y')
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



while True:
    screen.fill((255, 255, 255))
    screen.blit(bg_pic, bg)
    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if skin2.rect.x < x < skin2.rect.right and skin2.rect.y < y < skin2.rect.bottom:
                    game_state = 1 
        skin1.draw()
        skin2.draw()
    if game_state == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # обработка нажатий
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    player.x_speed = -5
                elif e.key == pygame.K_RIGHT:
                    player.x_speed = 5
                elif e.key == pygame.K_SPACE:
                    if not player.is_jump:
                        player.y_speed = -5
                        player.is_jump = True
                if e.key == pygame.K_e:
                    player.is_inventory_show = not player.is_inventory_show

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    player.x_speed = 0
                if e.key == pygame.K_SPACE:
                    player.y_speed = 2

        if player.is_jump:
            player.jump_time += 1
            if player.jump_time >= 180:
                player.y_speed = 2

        # движение обьектов
        player.move()


        #отрисовка объектов
        for wall in lvl1walls:
                    if player.iscollide(wall):
                        player.rect.y -= player.y_speed

                    if player.iscollide(wall):
                        player.rect.x -= player.x_speed


        if lvl == 1:

            for wall in lvl1walls:
                wall.draw()

            player.is_jump = True

            for wall in lvl1walls:
                if player.iscollide(wall):
                    player.rect.y -= player.y_speed
                    player.is_jump = False
                    player.jump_time = 0
                    player.y_speed = 2
                if player.iscollide(wall):
                    player.rect.x -= player.x_speed

        player.draw()

    pygame.display.update()
    clock.tick(FPS)