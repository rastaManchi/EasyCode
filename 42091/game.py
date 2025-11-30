import pygame
import os
import sys


pygame.init()
WIDTH = 500
HEIGHT = 500 
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 32)

#Классы
class Player:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        
    def draw(self):
        pygame.draw.rect(screen, (10, 10, 10), self.rect) # без скина
        screen.blit(self.img, self.rect) # со скином
        
class Clicker:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        
    def check_collide(self, mouse_pos):
        if mouse_pos.x > self.rect.x and mouse_pos.x < self.rect.right and mouse_pos.y > self.rect.y and mouse_pos.y < self.rect.bottom:
            print("Клик!")
        
    def draw(self):
        pygame.draw.rect(screen, (10, 10, 10), self.rect) # без скина
        screen.blit(self.img, self.rect) # со скином
        
class Button:
    def __init__(self, x, y, w, h, img, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.text = font.render(text, True, (255, 0, 0))
        
    def draw(self):
        pygame.draw.rect(screen, (10, 10, 10), self.rect) # без скина
        screen.blit(self.img, self.rect) # со скином 
        screen.blit(self.text, self.rect)
        
class Block:
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        
    def draw(self):
        pygame.draw.rect(screen, (10, 10, 10), self.rect) # без скина
        screen.blit(self.img, self.rect) # со скином
        
player = Player(0, 0 , 50, 50 , '.png')
button = Button(0 ,0 , 50 , 50 , '.png', 'text')
block = Block(0, 0 , 50, 50, '.png')
clicker = Clicker(0, 0 , 50, 50 , '.png')

while True:
    screen.fill((125, 125, 125))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            mouse_pos = {'x': mouse_pos[0], 'y': mouse_pos[1]}
            clicker.check_collide(mouse_pos)
            
    # движение обьектов 
    
    
    # рисовать обьекты
    button.draw()
    player.draw()
    clicker.draw()
    block.draw()
    
    pygame.display.update()
    clock.tick(FPS)