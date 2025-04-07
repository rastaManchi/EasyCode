import pygame
import random
import sys
import math

pygame.init()

WIDTH, HEIGHT = 500, 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30)

class Wall:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))


    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))


class Player:
    def __init__(self, x, y, w, h, img_path, walls):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.x_speed = 0
        self.y_speed = 0
        self.walls = walls


    def move(self):
        self.rect.x += self.x_speed
        for wall in self.walls:
            if self.collide(wall):
                self.rect.x -= self.x_speed

        self.rect.y += self.y_speed
        for wall in self.walls:
            if self.collide(wall):
                self.rect.y -= self.y_speed


    def collide(self, obj):
        return self.rect.colliderect(obj.rect)


    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))


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
        self.img_orig = pygame.transform.scale(self.img_orig, (w, h))
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
        
        x_to, y_to = to_point
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



    def move(self):
        self.float_x += self.x_speed
        self.float_y += self.y_speed
        self.rect.x = round(self.float_x)
        self.rect.y = round(self.float_y)

    
    def draw(self):
        screen.blit(self.img, self.rect)

    
    def rotate_to_point(self, mouse):
        dx, dy = mouse[0] - self.rect.centerx, mouse[1] - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - 90
        self.img = pygame.transform.rotate(self.img_orig, angle)
        self.rect = self.img.get_rect(center=self.rect.center)
        self.float_x = self.rect.x
        self.float_y = self.rect.y


    def collide(self, obj):
        return self.rect.colliderect(obj.rect)



lvl1walls = []
lvl2walls = []
lvl3walls = []
with open('lvl1.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl1walls.append(Wall(col * 20, row * 20, 20, 20, 'wall.png'))
            col += 1
        row += 1

with open('lvl2.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl2walls.append(Wall(col * 20, row * 20, 20, 20, 'wall.png'))
            col += 1
        row += 1

with open('lvl3.txt', 'r') as map:
    row, col = 0, 0
    for line in map.read().split('\n'):
        x = list(line)
        col = 0
        for i in x:
            if i == '1':
                lvl3walls.append(Wall(col * 20, row * 20, 20, 20, 'wall.png'))
            col += 1
        row += 1


player = Player(30, 30, 30, 30, 'knight.png', lvl1walls)

lvl1enemies = [
    Enemy(30, 80, 25, 25, 'creeper.png', 3, 30, 200, 'h'),
    Enemy(420, 50, 25, 25, 'creeper.png', 5, 50, 400, 'v')
]

lvl2enemies = []
lvl3enemies = []

bullets = []
level = 1

end_text = font.render('Вы прошли игру!', False, (0, 0, 0))

game_state = 1

while True:
    screen.fill((255, 255, 255))
    if game_state == 1:
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
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    player.x_speed = 0
                elif e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                    player.y_speed = 0
            elif e.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet(player.rect.centerx, player.rect.centery, 15, 15, 'bullet.png', e.pos)
                bullets.append(bullet)

            

        player.move()

        if level == 1:
            for enemy in lvl1enemies:
                enemy.move()

            for enemy in lvl1enemies:
                if player.collide(enemy):
                    player.rect.x = 30
                    player.rect.y = 30

            for wall in player.walls:
                wall.draw()

            for enemy in lvl1enemies:
                enemy.draw()


            if player.rect.x >= 500:
                level += 1
                player.walls = lvl2walls
                player.rect.x = 30
                player.rect.y = 30

            for wall in player.walls:
                for bullet in bullets:
                    if bullet.collide(wall):
                        bullets.remove(bullet)
                        break

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
            
            for bullet in bullets:
                if bullet.rect.x > 500 or bullet.rect.x <= -bullet.rect.width or bullet.rect.y >= 500 or bullet.rect.y <= -bullet.rect.height:
                    bullets.remove(bullet)
                    break


        if level == 2:
            for enemy in lvl2enemies:
                enemy.move()

            for enemy in lvl2enemies:
                if player.collide(enemy):
                    player.rect.x = 30
                    player.rect.y = 30

            for wall in player.walls:
                wall.draw()

            for enemy in lvl2enemies:
                enemy.draw()

            if player.rect.x >= 500:
                level += 1
                player.walls = lvl3walls
                player.rect.x = 30
                player.rect.y = 30

            for wall in player.walls:
                for bullet in bullets:
                    if bullet.collide(wall):
                        bullets.remove(bullet)
                        break

            for enemy in lvl2enemies:
                flag = False
                for bullet in bullets:
                    if bullet.collide(enemy):
                        bullets.remove(bullet)
                        flag = True
                        break
                if flag:
                    lvl2enemies.remove(enemy)
                    break
            
            for bullet in bullets:
                if bullet.rect.x > 500 or bullet.rect.x <= -bullet.rect.width or bullet.rect.y >= 500 or bullet.rect.y <= -bullet.rect.height:
                    bullets.remove(bullet)
                    break
            
        if level == 3:
            for enemy in lvl3enemies:
                enemy.move()

            for enemy in lvl3enemies:
                if player.collide(enemy):
                    player.rect.x = 30
                    player.rect.y = 30

            for wall in player.walls:
                wall.draw()

            for enemy in lvl3enemies:
                enemy.draw()

            for wall in player.walls:
                for bullet in bullets:
                    if bullet.collide(wall):
                        bullets.remove(bullet)
                        break

            for enemy in lvl3enemies:
                flag = False
                for bullet in bullets:
                    if bullet.collide(enemy):
                        bullets.remove(bullet)
                        flag = True
                        break
                if flag:
                    lvl3enemies.remove(enemy)
                    break
            
            for bullet in bullets:
                if bullet.rect.x > 500 or bullet.rect.x <= -bullet.rect.width or bullet.rect.y >= 500 or bullet.rect.y <= -bullet.rect.height:
                    bullets.remove(bullet)
                    break
            
            if player.rect.x >= 500:
                game_state = 2

        player.draw()

        for bullet in bullets:
            bullet.draw()
            bullet.move()

    elif game_state == 2:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
                
        screen.blit(end_text, (20, 230))

    
    pygame.display.update()
    clock.tick(60)