import pygame, sys, random

pygame.init()


WIDTH = 500
HEIGHT = 500
FPS = 60

WHITE = (255, 255, 255)
COLOR = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


player = pygame.Rect(0, 0, 50, 50)
player_orig_image = pygame.image.load('steve.png')
player_image = pygame.transform.scale(player_orig_image, (player.width, player.height))

direction = 'none'

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.x = 450
                player.y = 450
            if event.key == pygame.K_1:
                COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
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
                event.key == pygame.K_LEFT or \
                event.key == pygame.K_RIGHT or \
                event.key == pygame.K_DOWN:

                direction = 'none'
                

    
    if direction == 'left':
        player.x -= 5
    elif direction == 'right':
        player.x += 5
    elif direction == 'up':
        player.y -= 5
    elif direction == 'down':
        player.y += 5
        
    screen.blit(player_image, player)

    pygame.display.update()
    clock.tick(FPS)

