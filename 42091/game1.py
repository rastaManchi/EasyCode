import pygame, sys, random


pygame.init()


HEIGHT = 500
WIDTH = 500
FPS = 60
BACKGROUND = (150, 209, 227)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = pygame.Rect(0, 0, 50, 50)
player_orig_image = pygame.image.load("ufoBlue.png")
player_image = pygame.transform.scale(player_orig_image, (50, 50))

enemy = pygame.Rect(100, 100, 50, 50)
enemy_origin_image = pygame.image.load("ufoRed.png")
enemy_image = pygame.transform.scale(enemy_origin_image, (50, 50))

font = pygame.font.SysFont('Arial', 30)
start_text = font.render('Нажмите пробел, чтобы начать!', True, (0, 0, 0))

speed = 2
direction = None
game_state = 0

enemy_direction = None
while True:
    screen.fill(BACKGROUND)

    if game_state == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 1
        
        screen.blit(start_text, (20, 100))

    if game_state == 1:
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


        if player.colliderect(enemy):
            enemy.x = random.randint(0, WIDTH-enemy.width)
            enemy.y = random.randint(0, HEIGHT-enemy.height)
        
        screen.blit(player_image, player)
        
        screen.blit(enemy_image, enemy)

    pygame.display.update()
    clock.tick(FPS)
