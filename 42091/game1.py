import pygame, sys


HEIGHT = 500
WIDTH = 500
FPS = 60
BACKGROUND = (150, 209, 227)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(0, 0, 50, 50)
speed = 2
direction = None

while True:
    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 'right'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or \
                event.key == pygame.K_DOWN or \
                event.key == pygame.K_RIGHT or \
                event.key == pygame.K_LEFT:
                    direction = None


    if direction:
        if direction == 'right':
            player.x += speed
        elif direction == 'left':
            player.x -= speed
        elif direction == 'up':
            player.y -= speed
        elif direction == 'down':
            player.y += speed
    
    pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.update()
    clock.tick(FPS)
