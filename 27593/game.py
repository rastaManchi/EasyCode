import pygame, sys, random, time


pygame.init()


WIDTH = 500
HEIGHT = 500
FPS = 60
COLOR = (152, 47, 193)
DONIR = (255, 182, 193)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


player = pygame.Rect(0, 0, 50, 50)
player_orig_img = pygame.image.load('27593/SANS.png')
player_img = pygame.transform.scale(player_orig_img, (player.width, player.height))


enemy = pygame.Rect(100, 100, 50, 50)
enemy_orig_img = pygame.image.load('27593/steve.png')
enemy_img = pygame.transform.scale(enemy_orig_img, (enemy.width, enemy.height))


direction = 'none'
score = 0



while True:

    screen.fill(DONIR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if event.key == pygame.K_w:
                direction = 'up'
            elif event.key == pygame.K_s:
                direction = 'down'
            elif event.key == pygame.K_a:
                direction = 'left'
            elif event.key == pygame.K_d:
                direction = 'right'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or \
            event.key == pygame.K_s or \
            event.key == pygame.K_a or \
            event.key == pygame.K_d:
                direction = 'none'

    if direction == 'left':
        player.x -= 5
    elif direction == 'right':
        player.x += 5
    elif direction == 'up':
        player.y -= 5
    elif direction == 'down':
        player.y += 5
    
    if player.colliderect(enemy):
        enemy.x = random.randint(0, 450)
        enemy.y = random.randint(0, 450)
        player.width += 37
        player.height += 37
        player_img = pygame.transform.scale(player_orig_img, (player.width, player.height))
        score += 10
        print(score)

    if score >= 100:
        pygame.quit()
        sys.exit()

    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)
    # pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.update()
    clock.tick(FPS)
