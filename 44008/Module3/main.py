import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
lvl = 1

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

class Enemy:
    def __init__(self, x, y, w, h, img, speed, p1, p2, orientation):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.speed = speed
        if p1 > p2:
            p1, p2 = p2, p1
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

def generate_lvl():
    walls = []
    with open(f'lvl{lvl}.txt', 'r') as map:
        row, col = 0, 0
        for line in map.read().split('\n'):
            x = list(line)
            col = 0
            for i in x:
                if i == '1':
                    walls.append(Wall(col * 20, row * 20, 20, 20, 'wall.png'))
                col += 1
            row += 1
    return walls

walls = generate_lvl()
        
player = Player(25, 25, 20, 20, 5, 'knight.png')

enemies = [
    Enemy(350, 50, 20, 20, 'wall.png', 7, 50, 300, 'v'),
    Enemy(50, 400, 20, 20, 'wall.png', 4, 50, 300, 'h'),
]
    

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
    
    if player.rect.x >= WIDTH:
        lvl += 1
        player.rect.x = 50
        player.rect.y = 50
        walls = generate_lvl()
    elif player.rect.right <= 0:
        lvl -= 1
        player.rect.x = 50
        player.rect.y = 50
        walls = generate_lvl()
    
    if lvl == 1:
        for enemy in enemies:
            enemy.move()
            
        for enemy in enemies:
            if player.collide(enemy):
                pygame.quit()
                sys.exit()
                
        for enemy in enemies:
            enemy.draw()
    
    for wall in walls:
        if player.collide(wall):
            player.rect.x -= player.speedx
            player.rect.y -= player.speedy
    

    for wall in walls:
        wall.draw()
        
    player.draw()
    
    
    pygame.display.update()
    clock.tick(60)