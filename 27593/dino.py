import pygame
import sys
import random
import time

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60
last_cactus = time.time()

#классы
class Dino:
    def __init__(self, x, y, w, h, img, inventory=[]):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.x_speed = 0
        self.y_speed = 0
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
        screen.blit(self.img, self.rect)

class Cactus(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.speed = 2
    
    def move(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.kill() 

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

#создание экземпляров
dino = Dino(50, 400, 30, 70, '27593/wall.jpg')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cactuses = []

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # обработка нажатий

    if time.time() - last_cactus > random.randint(5, 10):
        last_cactus = time.time()
        cactuses.append(Cactus(WIDTH, 400, 30, 70, (0, 255, 0)))

    # движение обьектов
    for cactus in cactuses:
        cactus.move()
        cactus.draw()


    #отрисовка объектов
    dino.draw()
    

    pygame.display.update()
    clock.tick(FPS)