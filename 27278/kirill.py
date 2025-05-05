import pygame
import random
import sys
import os
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash Mini")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

player_img = pygame.image.load(os.path.join('Кубик геометри Деш.png'))
player_img = pygame.transform.scale(player_img, (40, 40))

clock = pygame.time.Clock()
FPS = 60
GRAVITY = 0.8
JUMP_FORCE = -15
GAME_SPEED = 5
font = pygame.font.SysFont('Arial', 30)
score = 0

background = pygame.image.load(os.path.join('бг гд.png'))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


pygame.mixer.music.load('Firework [4K] - Geometry Dash.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.06)

exit_button_rect = pygame.Rect(WIDTH - 110, 10, 100, 40)

class Player:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.x = 100
        self.y = HEIGHT // 2
        self.vel_y = 0
        self.is_jumping = False
        self.color = BLUE

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

        if self.y >= HEIGHT - self.height:
            self.y = HEIGHT - self.height
            self.vel_y = 0
            self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = JUMP_FORCE
            self.is_jumping = True

    def draw(self):
        if player_img:
            screen.blit(player_img, (self.x, self.y))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class Obstacle:
    def __init__(self):
        self.width = 25
        self.height = random.randint(50, 85)
        self.x = WIDTH
        self.y = HEIGHT - self.height
        self.color = RED

    def update(self):
        self.x -= GAME_SPEED

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def is_off_screen(self):
        return self.x < -self.width

    def collides_with(self, player):
        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
        obstacle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return player_rect.colliderect(obstacle_rect)


def game_loop():
    global score, GAME_SPEED, background

    player = Player()
    obstacles = []
    obstacle_timer = 0
    obstacle_frequency = 1500
    last_obstacle_time = pygame.time.get_ticks()
    game_over = False
    score = 0

    while True:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_r and game_over:
                    return game_loop()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        if not game_over:
            player.update()

            if current_time - last_obstacle_time > obstacle_frequency:
                obstacles.append(Obstacle())
                last_obstacle_time = current_time

                if score % 5 == 0:
                    GAME_SPEED += 0.5
                    obstacle_frequency = max(800, obstacle_frequency - 50)
                
                if score == 15:
                    background = pygame.image.load(os.path.join('бг гд1.png'))
                    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

            for obstacle in obstacles[:]:
                obstacle.update()

                if obstacle.collides_with(player):
                    game_over = True

                if obstacle.is_off_screen():
                    obstacles.remove(obstacle)
                    score += 1  

                

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, WHITE, (0, HEIGHT - 10, WIDTH, 10))

        player.draw()
        for obstacle in obstacles:
            obstacle.draw()

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.draw.rect(screen, RED, exit_button_rect)
        exit_text = font.render("Exit", True, WHITE)
        screen.blit(exit_text, (exit_button_rect.x + 20, exit_button_rect.y + 5))

        if game_over:
            game_over_text = font.render("Game Over! Press R to restart", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - 180, HEIGHT // 2 - 15))

        pygame.display.update()
        clock.tick(FPS)

game_loop()