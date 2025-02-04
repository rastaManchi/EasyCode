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
player_orig_image = pygame.image.load('26847/SANS.png')
player_image = pygame.transform.scale(player_orig_image, (player.width, player.height))


player2 = pygame.Rect(100, 100, 150, 150)
player2_orig_image = pygame.image.load('26847/steve.png')
player2_image = pygame.transform.scale(player2_orig_image, (player2.width, player2.height))


diamond = pygame.Rect(450, 450, 20, 20)

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

    if player.colliderect(player2) and player.width > player2.width:
        player.width += player2.width
        player.height += player2.height
        player_image = pygame.transform.scale(player_orig_image, (player.width, player.height))
        player2.x = random.randint(0, 450)
        player2.y = random.randint(0, 450)

    if player.colliderect(diamond):
        player.width += 15
        player.height += 15
        player_image = pygame.transform.scale(player_orig_image, (player.width, player.height))
        diamond.x = random.randint(0, 450)
        diamond.y = random.randint(0, 450)
        
    screen.blit(player_image, player)
    screen.blit(player2_image, player2)
    pygame.draw.rect(screen, (0, 0, 255), diamond)

    pygame.display.update()
    clock.tick(FPS)

