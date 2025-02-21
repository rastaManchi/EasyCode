import pygame # подключаем библиотеку
import sys # подключаем модуль для 
from random import *
import os, math

score = 0 
if os.path.exists('23963/nickname.txt'):
    file = open('23963/nickname.txt', 'r')
    best_score = int(file.read())
    file.close()
else:
    print('Файла нет')

lvl1walls = []

if os.path.exists('23963/lvl1.txt'):
    row = 0
    col = 0
    file = open('23963/lvl1.txt', 'r')
    map_lines = file.readlines()
    for line in map_lines:
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl1walls.append(pygame.Rect(col*20, row*20, 20, 20))
                print(col, row)
            col += 1
        row += 1

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Enemy:
    def __init__(self, x, y, w, h, img_path, speed, p1, p2, orient):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.speed = speed
        self.p1 = p1
        self.p2 = p2
        self.orient = orient

    def move(self):
        if self.orient == 'h':
            self.rect.x += self.speed
            if self.rect.x >= self.p2 or self.rect.x <= self.p1:
                self.speed *= -1
        else:
            self.rect.y += self.speed
            if self.rect.y >= self.p2 or self.rect.y <= self.p1:
                self.speed *= -1

    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Bullet:
    def __init__(self, x, y, w, h, img_path, mouse):
        self.rect = pygame.Rect(x, y, w, h)
        self.img_orig = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img_orig, (w, h))
        self.x_speed = 0
        self.y_speed = 0
        self.default_speed = 3
        self.mouse = mouse
        self.float_x = x
        self.float_y = y
        self.set_speed(mouse)
    
    def set_speed(self, to_point):
        x_from, y_from = self.rect.centerx, self.rect.centery
        x_to , y_to = to_point
        dx = x_to - x_from
        dy = y_to - y_from
        x_speed = round(abs((self.default_speed * dx) / math.sqrt(dx**2 + dy**2)), 3)
        y_speed = round(abs((x_speed * dy) / dx), 3)
        if x_to < x_from:
            x_speed *= -1
        if y_to < y_from:
            y_speed *= -1

        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotate_to_point(self.mouse)

    def rotate_to_point(self, mouse):
        dx, dy = mouse[0] - self.rect.centerx, mouse[1] - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - 90
        self.img = pygame.transform.rotate(self.img, angle)
        self.rect = self.img.get_rect(center=self.rect.center)
        self.float_x = self.rect.x
        self.float_y = self.rect.y

    def move(self):
        self.float_x += self.x_speed
        self.float_y += self.y_speed
        self.rect.x = round(self.float_x)
        self.rect.y = round(self.float_y)

    def draw(self):
        screen.blit(self.img, self.rect)

    def collide(self, obj):
        return self.rect.colliderect(obj.rect)

    

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
lvl1enemies = [
    Enemy(30, 80, 25, 25, '23963/SANS.png', 3, 30, 200, 'h'),
    Enemy(420, 50, 25, 25, '23963/SANS.png', 5, 50, 400, 'v')
]
button = Sprite(0, 0, 50, 50, '23963/close_btn.png')
skin1 = Sprite(100, 225, 50, 50, '23963/steve.png')
skin2 = Sprite(225, 225, 50, 50, '23963/knight.png')
skin3 = Sprite(350, 225, 50, 50, '23963/SANS.png')
bg = Sprite(0, 0 , 500, 500, '23963/steve.png')

game_state = 0

font = pygame.font.SysFont('Arial', 30)
score_font = pygame.font.SysFont('Arial', 15)

start_text = font.render('Выбери скин!', False, (255, 0, 0))
end_text = font.render('Игра окончена', False, (0, 255, 0))

score_text = score_font.render(f'Кол-во очков: {score}', False, (255, 0, 0))
best_score_text = score_font.render(f'Рекорд {best_score}', False, (255, 0, 0))

restart_text_1 = font.render('Пробел, чтобы', False, (100, 150, 0))
restart_text_2 = font.render('перезапустить игру!', False, (100, 150, 0))


bullets = []
level = 1
 

while True:
    screen.blit(bg.img, bg.rect)
    # screen.fill((0, 0, 0))
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
                else:
                    bullet = Bullet(player.rect.centerx, player.rect.centery, 15, 15, '23963/steve.png', e.pos)
                    bullets.append(bullet)

        for bullet in bullets:
            if bullet.rect.x > 500 or bullet.rect.x <= -bullet.rect.width or bullet.rect.y >= 500 or bullet.rect.y <= -bullet.rect.height:
                bullets.remove(bullet)
            bullet.draw()
            bullet.move()

        player.move()

        if level == 1:
            for enemy in lvl1enemies:
                enemy.move()

            for enemy in lvl1enemies:
                enemy.draw()

            for enemy in lvl1enemies:
                flag = False
                for bullet in bullets:
                    if bullet.collide(enemy):
                        bullets.remove(bullet)
                        flag = True
                        break
                if flag:
                    lvl1enemies.remove(enemy)
                    break
            
            for wall in lvl1walls:
                if player.collide(wall):
                    player.rect.x -= player.x_speed
                    player.rect.y -= player.y_speed

            for wall in lvl1walls:
                pygame.draw.rect(screen, (255, 0, 0), wall)

        # if player.rect.colliderect(enemy.rect):
        #     enemy.rect.x = randint(0, 470)
        #     enemy.rect.y = randint(0, 470)
        #     player.rect.width += 10
        #     player.rect.height += 10
        #     player.img = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
        #     score += randint(1, 10)
        #     score_text = score_font.render(f'Кол-во очков: {score}', False, (255, 0, 0))
            

        if player.rect.width >= 300:
            if best_score < score:
                file = open('23963/nickname.txt', 'w', encoding='UTF-8')
                file.write(str(score))
                file.close()
            game_state = 2


        player.draw()
        button.draw()
        screen.blit(score_text, (100, 50))
        screen.blit(best_score_text, (300, 50))
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