import pygame, sys

pygame.init()
HEIGH = 500
WIDTH = 500
FPS = 30

game_status = 0

screen = pygame.display.set_mode((WIDTH, HEIGH))
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 30)
start_text = font.render('Нажмите на пробел', True, (0, 255, 0))
end_text = font.render('Нажмите q, чтобы выйти', True, (255, 0, 0))

while True:
    if game_status == 0:
        screen.fill((100, 100, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_status = 1
        
        screen.blit(start_text, (20, 255))
    elif game_status == 1:
        screen.fill((150, 100, 150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    game_status = 2
        
        # движение игрока
        # отрисовка игрока
    elif game_status == 2:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            
        screen.blit(end_text, (20, 255))
    pygame.display.update()
    clock.tick(FPS)