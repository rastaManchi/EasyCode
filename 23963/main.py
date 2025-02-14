import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *
import os

score = 0 
if os.path.exists('23963/nickname.txt'):
    file = open('23963/nickname.txt', 'r')
    best_score = int(file.read())
    file.close()
else:
    print('Файла нет')

walls = []

if os.path.exists('23963/map.txt'):
    row = 0
    col = 0
    file = open('23963/map.txt', 'r')
    map_lines = file.readlines()
    for line in map_lines:
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                walls.append(pygame.Rect(col*20, row*20, 20, 20))
                print(col, row)
            col += 1
        row += 1

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Sprite:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.x_speed = 0
        self.y_speed = 0

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        

    def draw(self):
        screen.blit(self.img, self.rect)

    def collide(self, obj):
        return self.rect.colliderect(obj)

player = Sprite(225, 225, 50, 50, '23963/steve.png')
enemy = Sprite(50, 50, 30, 30, '23963/SANS.png')
button = Sprite(0, 0, 50, 50, '23963/close_btn.png')
skin1 = Sprite(100, 225, 50, 50, '23963/steve.png')
skin2 = Sprite(225, 225, 50, 50, '23963/knight.png')
skin3 = Sprite(350, 225, 50, 50, '23963/SANS.png')

game_state = 0

font = pygame.font.SysFont('Arial', 30)
score_font = pygame.font.SysFont('Arial', 15)

start_text = font.render('Выбери скин!', False, (255, 0, 0))
end_text = font.render('Игра окончена', False, (0, 255, 0))

score_text = score_font.render(f'Кол-во очков: {score}', False, (255, 0, 0))
best_score_text = score_font.render(f'Рекорд {best_score}', False, (255, 0, 0))

restart_text_1 = font.render('Пробел, чтобы', False, (100, 150, 0))
restart_text_2 = font.render('перезапустить игру!', False, (100, 150, 0))

 

while True:
    screen.fill((0, 0, 0))
    if game_state == 0:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if skin1.rect.x <= x <= skin1.rect.right and skin1.rect.y <= y <= skin1.rect.bottom:
                    player.orig_img = pygame.image.load('23963/steve.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                if skin2.rect.x <= x <= skin2.rect.right and skin2.rect.y <= y <= skin2.rect.bottom:
                    player.orig_img = pygame.image.load('23963/knight.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                if skin3.rect.x <= x <= skin3.rect.right and skin3.rect.y <= y <= skin3.rect.bottom:
                    player.orig_img = pygame.image.load('23963/SANS.png')
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
        screen.blit(start_text, (20, 155))
        skin1.draw()
        skin2.draw()
        skin3.draw()
    elif game_state == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    player.x_speed = 5
                elif e.key == pygame.K_LEFT:
                    player.x_speed = -5
                elif e.key == pygame.K_UP:
                    player.y_speed = -5
                elif e.key == pygame.K_DOWN:
                    player.y_speed = 5
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    player.y_speed = 0
                elif e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    player.x_speed = 0
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = e.pos
                if 0 < x < 50 and 0 < y < 50:
                    sys.exit()

        player.move()

        if player.rect.colliderect(enemy.rect):
            enemy.rect.x = randint(0, 470)
            enemy.rect.y = randint(0, 470)
            player.rect.width += 10
            player.rect.height += 10
            player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
            score += randint(1, 10)
            score_text = score_font.render(f'Кол-во очков: {score}', False, (255, 0, 0))
            

        if player.rect.width >= 300:
            if best_score < score:
                file = open('23963/nickname.txt', 'w', encoding='UTF-8')
                file.write(str(score))
                file.close()
            game_state = 2

        for wall in walls:
            if player.collide(wall):
                player.rect.x -= player.x_speed
                player.rect.y -= player.y_speed

        for wall in walls:
            pygame.draw.rect(screen, (255, 0, 0), wall)

        player.draw()
        enemy.draw()
        button.draw()
        screen.blit(score_text, (100, 0))
        screen.blit(best_score_text, (300, 0))
    elif game_state == 2:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    player.rect.x = 255
                    player.rect.y = 255
                    player.rect.width = 50
                    player.rect.height = 50
                    player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    player.x_speed = 0
                    player.y_speed = 0
                    enemy.rect.x = 50
                    enemy.rect.y = 50
                    game_state = 0
        screen.blit(end_text, (20, 255))
        screen.blit(restart_text_1, (20, 300))
        screen.blit(restart_text_2, (20, 345))

    pygame.display.update()
    clock.tick(60)