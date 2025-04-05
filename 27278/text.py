import pygame
import os
import sys

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


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
    
    def texture_draw(self):
        screen.blit(self.img, self.rect)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def move(self):
        if self.orientation == 'x':
            self.rect.x += self.speed
            if self.rect.x >= self.p2 or self.rect.x <= self.p1:
                self.speed = -self.speed
        if self.orientation == 'y':
            self.rect.y += self.speed
            if self.rect.y >= self.p2 or self.rect.y <= self.p1:
                self.speed = -self.speed

class Wall():
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Player:
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.x_speed = 0
        self.y_speed = 0

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


walls = []

if os.path.exists('27278/map.txt'):
    file = open('27278/map.txt', 'r', encoding='utf-8')
    lines = file.read().split('\n')
    current_row = 0
    for line in lines:
        row_list = list(line)
        current_column = 0
        for x in row_list:
            if x == '1':
                walls.append(Wall(current_column*20, current_row*20, 20, 20, (0, 0, 0)))
                print(current_column, current_row)
            elif x == 'P':
                player = Player(current_column*20, current_row*20, 20, 20, (255, 0, 0))
            current_column += 1
        current_row += 1
else:
    print('Файл уровня не найден!')

enemy = Enemy(30, 30, 20, 20, (255, 0, 0), '27278/steve.png', 30, 120, 'x')


while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_speed = -5
            elif event.key == pygame.K_RIGHT:
                player.x_speed = 5
            if event.key == pygame.K_DOWN:
                player.y_speed = 5
            elif event.key == pygame.K_UP:
                player.y_speed = -5 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.y_speed = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_speed = 0

    for wall in walls:
        wall.draw()

    player.move()
    enemy.move()

    for wall in walls:
        if player.rect.colliderect(wall.rect):
            player.rect.x -= player.x_speed
            player.rect.y -= player.y_speed

    player.draw()
    enemy.draw()

    pygame.display.update()
    clock.tick(FPS)




