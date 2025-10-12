import pygame, sys


HEIGHT = 500
WIDTH = 500
FPS = 60
BACKGROUND = (150, 209, 227)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.speedx = 2
        self.speedy = 0

    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

player = Player(0,0,50,50)
speed = 2

while True:
    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

    player.move()

    if player.rect.x >= 450:
        player.speedx = -speed
    elif player.rect.x < 0:
        player.speedx = speed
    
    player.draw()

    pygame.display.update()
    clock.tick(FPS)