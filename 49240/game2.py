import pygame
import sys


pygame.init()

WIDTH = 500
HEIGHT = 500
BG = (100, 100, 100)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, w, h, speed, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed
        self.img_orig = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img_orig, (w, h))
        self.direction = None
        
    def move(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
            
    def draw(self):
        screen.blit(self.img, self.rect)
        

player = Player(10, 10, 50, 50, 5, 'player.png')


while True:
    screen.fill(BG)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: player.direction = 'left'
            elif event.key == pygame.K_RIGHT: player.direction = 'right'
            elif event.key == pygame.K_UP: player.direction = 'up'
            elif event.key == pygame.K_DOWN: player.direction = 'down'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT \
                or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP \
                        or event.key == pygame.K_DOWN:
                            player.direction = None
            
    
    player.move()
    player.draw()
    

    pygame.display.update()
    clock.tick(120)