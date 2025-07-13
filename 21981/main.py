import pygame
import sys


WIDTH = 500
HEIGHT = 500
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GRAY = (202, 204, 206)
RED = (255, 0, 0)

pygame.init()

class Player():
    def __init__(self, w, h, x, y, xspeed, yspeed, imgpath):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_image = pygame.image.load(imgpath)
        self.image = pygame.transform.scale(self.orig_image, (w, h))
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.jump_count = 0
        self.max_jumps = 20
        self.is_jump = False
        
    def move(self):
        self.rect.x += self.xspeed
        
    def jump(self):
        if self.is_jump:
            self.yspeed = -5
            self.jump_count += 1
            if self.jump_count >= self.max_jumps:
                self.yspeed = 5
                self.is_jump = False
                self.jump_count = 0
        self.rect.y += self.yspeed

    def draw(self):
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, RED, self.rect)
        
class Block:
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        
    def collide(self, obj: Player):
        if self.rect.colliderect(obj.rect):
            if obj.rect.y <= self.rect.y - obj.rect.height + 10:
                obj.is_jump = True
                
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

player = Player(50, 50, 0, 0, 5, 5, 'player.png')

block1 = Block(100, 200, 150, 50, (0, 255, 0))

while True:
    screen.fill(GRAY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.xspeed = -5
            elif event.key == pygame.K_d:
                player.xspeed = 5
            if event.key == pygame.K_SPACE:
                player.is_jump = True
                
    player.move()
    player.jump()
    block1.collide(player)
    
    block1.draw()
    player.draw()

            
    pygame.display.update()
    clock.tick(FPS)