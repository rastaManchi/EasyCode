import pygame
import sys 

pygame.init()


WIDTH = 500
HEIGHT = 500

font = pygame.font.SysFont("Arial", 25)
start_text = font.render('Нажмите на пробел', True, (100, 100, 0))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


BG = (169, 255, 156)
COLOR = (255, 97, 48)

player = pygame.Rect(0, HEIGHT/2, 100, 100)
enemy = pygame.Rect(0, HEIGHT, 100, 100)

direction = 'none'

# 0 - меню / 1 - игра / 2 - конец 
game_state = 0


while True:
    # Задний фон
    screen.fill(BG)
    
    if game_state == 0:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 1
        
        screen.blit(start_text, (20, HEIGHT-40))
    
    elif game_state == 1:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:COLOR = (206,71,255)
                elif event.key == pygame.K_2: COLOR = (71,123,255)
                
                elif event.key == pygame.K_3: COLOR = (3,163,0)
                elif event.key == pygame.K_4: COLOR = (224,161,0)
                elif event.key == pygame.K_LEFT: direction = 'left'
                elif event.key == pygame.K_RIGHT: direction = 'right'
                elif event.key == pygame.K_UP: direction = 'up'
                elif event.key == pygame.K_DOWN: direction = 'down'
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT \
                    or event.key == pygame.K_RIGHT \
                        or event.key == pygame.K_UP \
                            or event.key == pygame.K_DOWN:
                                direction = 'none'
                
                
        #Движение
        if direction == 'left': player.x -= 5
        elif direction == 'right': player.x += 5
        elif direction == 'up': player.y -= 5
        elif direction == 'down': player.y += 5
                
        if player.colliderect(enemy):
            sys.exit()
        
        # Отрисовка
        pygame.draw.rect(screen, COLOR, player)
        pygame.draw.rect(screen, COLOR, enemy)

    # Обновление экрана
    pygame.display.update()
    clock.tick(60)