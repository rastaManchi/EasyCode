import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BG = (144, 0, 255)
player = pygame.Rect(250, 250, 50, 50)
player_img = pygame.image.load('player.jpg')
player_img = pygame.transform.scale(player_img, (player.width, player.height))
direction = ''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = 'up'
            elif event.key == pygame.K_s:
                direction = 'down'
            elif event.key == pygame.K_a:
                direction = 'left'
            elif event.key == pygame.K_d:
                direction = 'right'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                direction = ''
    screen.fill(BG)
    if direction == 'up':
        player.y -= 5
    elif direction == 'down':
        player.y += 5
    elif direction == 'left':
        player.x -= 5
    elif direction == 'right':
        player.x += 5
    screen.blit(player_img, player)
    pygame.display.update()
    clock.tick(60)