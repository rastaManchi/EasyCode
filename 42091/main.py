import pygame
import os
import sys


pygame.init()
WIDTH = 500
HEIGHT = 500 
FPS = 60
lvl = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Wall:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x,y,w,h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        
    def draw(self):
        screen.blit(self.img, self.rect)


class Player:
    def __init__(self, x, y, w, h, img, walls):
        self.rect = pygame.Rect(x,y,w,h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.speed_x = 0
        self.speed_y = 0
        self.walls = walls
        
    def move(self):
        self.rect.x += self.speed_x
        for wall in self.walls:
            if self.collide(wall):
                self.rect.x -= self.speed_x
                
        self.rect.y += self.speed_y
        for wall in self.walls:
            if self.collide(wall):
                self.rect.y -= self.speed_y
                
    def collide(self, obj):
        return self.rect.colliderect(obj.rect)
    
    def draw(self):
        screen.blit(self.img, self.rect)
        

class Enemy:
    def __init__(self, x, y, w, h, img, speed, p1, p2, orientation):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w,h))
        self.speed = speed
        self.p1 = p1
        self.p2 = p2
        self.orientation = orientation
        
    def move(self):
        if self.orientation == 'h':
            self.rect.x += self.speed
            if self.rect.x >= self.p2 or self.rect.x <= self.p1:
                self.speed *= -1
        else:
            self.rect.y += self.speed
            if self.rect.y >= self.p2 or self.rect.y <= self.p1:
                self.speed *= -1
                
    def draw(self):
        screen.blit(self.img, self.rect)

lvl_map = []

def generate_lvl(lvl):
    lvl_map = []
    if os.path.exists(f"lvl{lvl}.txt"):
        file = open(f'lvl{lvl}.txt', 'r')
        stroki = file.read().split('\n')
        row = 0
        for stroka in stroki:
            symbols = list(stroka)
            col = 0
            for symbol in symbols:
                if symbol == "1":
                    wall = Wall(20*col, 20*row, 20, 20, "wall.webp")
                    lvl_map.append(wall)
                col += 1
            row += 1
    return lvl_map

lvl_map = generate_lvl(lvl)
print(lvl_map)

player = Player(30, 30, 20, 20, 'wall.webp', lvl_map)

lvl1enemies = [
    Enemy(30, 80, 25, 25, 'wall.webp', 3, 30, 200, 'h'),
    Enemy(420, 50, 25, 25, 'wall.webp', 5, 50, 400, 'v')
]


while True:
    
    screen.fill((125, 125, 125))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
            elif event.key == pygame.K_UP:
                player.speed_y = -5
            elif event.key == pygame.K_DOWN:
                player.speed_y = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.speed_y = 0
    
    player.move()
    
    if player.rect.x > WIDTH:
        lvl += 1
        lvl_map = generate_lvl(lvl)
        player.rect.x = 30
        player.rect.y = 30
        player.walls = lvl_map
    elif player.rect.right < 0:
        lvl -= 1
        lvl_map = generate_lvl(lvl)
        player.rect.x = 30
        player.rect.y = 30
        player.walls = lvl_map
    
    for wall in lvl_map:
        wall.draw()
        
    if lvl == 1:
        for enemy in lvl1enemies:
            enemy.move()
        
        for enemy in lvl1enemies:
            enemy.draw()
        
    player.draw()
    
    pygame.display.update()
    clock.tick(FPS)