import pygame 
import sys 
import random 
import time 

pygame.init()

WIDTH = 500
HEIGHT = 500
FPS = 60

last_cactus = time.time()


class Dino:
    def __init__(self, x, y, w, h, img ):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (w, h))
        self.x_speed = 0
        self.y_speed = 0

        self.jamp_time = 0 
        self.is_jamp = False
                
        
        
    def jamp (self):
        if not self.is_jamp:
            self.is_jamp = True
            self.y_speed = -2
    
    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.y <= 200:
            self.y_speed = -self.y_speed
        elif self.rect.y >= 400:
            self.rect.y = 400
            self.y_speed = 0
            self.is_jamp = False
            
        

        
    
    def iscollide(self, obj: pygame.Rect):
        if self.rect.colliderect(obj):
            return True
        return False

    def draw(self):
        screen.blit(self.img, self.rect)



class Cactus (pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, img):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img  = pygame.image.load(img)
        self.img = pygame.transform.scale(self.orig_img, (self.rect.width, self.rect.height))

        self.speed = 2

    def move (self):
        self.rect.x -= self.speed 
        if self.rect.right <= 0:
            self.kill()
        
    def draw (self):
         screen.blit(self.img, self.rect)

            
    
            
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


dino = Dino(50 , 400 , 60  ,80 , '777/DinoDead.png' ) 
cactuses = []


while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino.jamp()
                
    if time.time() - last_cactus > random.randint(5,10):
        last_cactus = time.time()
        cactuses.append(Cactus(WIDTH , 400 , 30 , 70 , '777/LargeCactus1.png'))
        
        
    for cactus in cactuses:
        cactus.move()
        cactus.draw()

    dino.move() 
    
    dino.draw()


    pygame.display.update()
    clock.tick(FPS)