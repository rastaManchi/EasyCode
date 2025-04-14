import pygame, sys

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)

#классы
class Stone():
    def __init__(self, x, y, w, h, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))

class Btn():
    def __init__(self, x, y, w, h, name, lvl, price, img):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.name = name
        self.lvl = lvl
        self.price = price

class Player():
    def __init__(self, money, clicks):
        self.money = money
        self.clicks = clicks



#Экземепляры классов
player = Player(100, 0)
bnts = [
    Btn(0, 0, 200, 50, 'Привет', 1, 100, '*.img'),
    Btn(60, 0, 200, 50, 'Привет', 2, 500, '*.img')
]
stone = Stone(250, 250, 100, 100, '*.png')


while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # дополнительные условия
    
    #движение обьектов

    #отрисовка обьектов


    pygame.display.update()
    clock.tick(FPS)