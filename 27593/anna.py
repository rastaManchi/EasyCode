import pygame
import sys
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60
game_state = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 15)

# фон
# from PL import Image, ImageTK
# import tkinter as tk 
# root = tk.TK()
# image = Image.open("s.png")
# photo = ImageTK.PhotoImage(image)
# label = tk.Label(root, image=photo)
# label.pack()
# root.mainloop() [5]('s.png')

#классы
class Wall:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))

    def draw(self):
        screen.blit(self.img, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

class Enemy:
    def __init__(self, x, y, w, h, clor, img, p1, p2, orien ):
        self.rect = pygame.Rect(x, y, w, h)
        self.clor = clor
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w,h))
        if p1 > p2:
            p1, p2 = p2, p1
        self.p1 =p1
        self.p2 = p2
        self.orien = orien
        self.speed = 5

    def draw_without_img(self):
        pygame.draw.rect(screen, self.clor, self.rect) 

    def move(self):
        if self.orien == 'x':
            if self.p1 > self.rect.x or self.p2 < self.rect.x:
                self.speed = -self.speed
            self.rect.x += self.speed
        elif self.orien == 'y':
            if self.p1 > self.rect.y or self.p2 < self.rect.y:
                self.speed = -self.speed
            self.rect.y += self.speed


class Button():
    def __init__(self, x, y, w, h, color, text, sobitie):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = font.render(text, True, (255, 255, 255))
        self.sobitie = sobitie

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, (self.rect.x + 20, self.rect.y + self.rect.height//2 - 7))


class Player:
    def __init__(self, x, y, w, h, img, speed):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.x_speed = 0
        self.y_speed = 0
        self.speed = speed
        # self.frace = 1
        # self.max_frace = 3
    
    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
    
    def iscollide(self, obj: pygame.Rect):
        if self.rect.colliderect(obj):
            return True
        return False
    def draw(self):
        screen.blit(self.img, self.rect)

    # def draw(self):
    #     self.frace += 1
    #     if self.max_frace < self.frace:
    #         self.frace = 1
    #     print(self.frace, f'анимация{self.frace}.png')
    #     # self.orig_img = pygame.image.load(f'анимация{self.frace}.png')
    #     # self.img = pygame.transform.scale(self.orig_img, (self.rect.width, self.rect.height))
    #     screen.blit(self.img, self.rect)


#создание экземпляров
walls = []
file  = open('game3.txt', 'r', encoding='utf-8')
lines = file.read().split('\n')
row = 0
for line in lines:
    items = list(line)
    column = 0
    for x in items:
        if x == '1':
            walls.append(Wall(column*20, row*20, 20, 20, 'pay.jpg'))
        column += 1
    row += 1  

buttons = [
    Button(0, 0, 100, 50, (0, 255, 0), 'Привет', 'Hello'),
    Button(0, 60, 100, 50, (0, 255, 0), 'Как дела', 'How are you')
]
player = Player(20, 20, 75, 75, 'pay.jpg', 'none')
# enemy = Enemy(20, 20, 75, 75, 'pay.jpg', 'none')



while True:
    screen.fill((255, 255, 255))

    if game_state == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for button in buttons:
                    if button.rect.x < x < button.rect.right and button.rect.y < y < button.rect.bottom:
                        if button.sobitie == 'Hello':
                            print('Начался бой!')
                            game_state = 1
                        elif button.sobitie == 'How are you':
                            print('Пощада')
                    
        for button in buttons:
            button.draw()
    # движение обьектов
    if game_state == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    player.x_speed = -5
                elif e.key == pygame.K_d:
                    player.x_speed = 5
                if e.key == pygame.K_w:
                    player.y_speed = -5
                elif e.key == pygame.K_s:
                    player.y_speed = 5
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_a or e.key == pygame.K_d:
                    player.x_speed = 0
                if e.key == pygame.K_w or e.key == pygame.K_s:
                    player.y_speed = 0

    #отрисовка объектов
        

        for wall in walls:
                wall.draw()
        for wall in walls:
                if player.iscollide(wall):
                    player.rect.x -= player.x_speed
                    player.rect.y -= player.y_speed
          

        player.draw()
    
        player.move()
    

    pygame.display.update()
    clock.tick(FPS)