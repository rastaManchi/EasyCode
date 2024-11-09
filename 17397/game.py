import pygame
import sys

pygame.init()
game_state = 0

WIDTH = 500
HEIGHT = 500


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


font = pygame.font.SysFont('Arial', 30)
start_text_1 = font.render('Добро пожаловать!', False, (255, 0, 0))
start_text_2 = font.render('Нажмите пробел, чтобы начать.', False, (255, 0, 0))

end_text_1 = font.render('Вы прошли игру! Нажмите пробел,', False, (0, 255, 0))
end_text_2 = font.render('чтобы начать заново.', False, (0, 255, 0))

BG = (144, 0, 255)


class Sprite:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.orig_img = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.orig_img, (w, h))
        self.direction = 'none'

    def move(self):
        if self.direction == 'up':
            self.rect.y -= 5
        elif self.direction == 'down':
            self.rect.y += 5
        elif self.direction == 'left':
            self.rect.x -= 5
        elif self.direction == 'right':
            self.rect.x += 5

    def draw(self):
        screen.blit(self.image, self.rect)


enemy = Sprite(50, 50, 50, 50, 'enemy.png')
player = Sprite(250, 250, 50, 50, 'player.png')

skin1 = Sprite(100, 225, 50, 50, 'player.png')
skin2 = Sprite(225, 225, 50, 50, 'enemy.png')


while True:
    if game_state == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 2
                    # player.rect.x, player.rect.y, player.rect.width, player.rect.height = 400, 400, 50, 50
                    # enemy.rect.x, enemy.rect.y = 50, 50
                    # player.image = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    # game_state = 1
        screen.blit(start_text_1, (20, 225))
        screen.blit(start_text_2, (20, 255))
    if game_state == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if skin2.rect.x <= x <= skin2.rect.right and skin2.rect.y <= y <= skin2.rect.bottom:
                    player.orig_img = pygame.image.load('enemy.png')
                    player.image = pygame.transform.scale(player.orig_img, (player.rect.width, player.rect.height))
                    game_state = 1
                if skin1.rect.x <= x <= skin1.rect.right and skin1.rect.y <= y <= skin1.rect.bottom:
                    game_state = 1
        skin1.draw()
        skin2.draw()
    if game_state == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.direction = 'up'
                elif event.key == pygame.K_s:
                    player.direction = 'down'
                elif event.key == pygame.K_a:
                    player.direction = 'left'
                elif event.key == pygame.K_d:
                    player.direction = 'right'
                elif event.key == pygame.K_1:
                    player.width = player.width * 2
                    player.height = player.height * 2
                    player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))
                elif event.key == pygame.K_2:
                    player.width = player.width * 0.5
                    player.height = player.height * 0.5
                    player_img = pygame.transform.scale(player_img_orig, (player.width, player.height))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                    direction = ''
        screen.fill(BG)
        player.move()
        player.draw()
        enemy.draw()
        if player.rect.colliderect(enemy):
            sys.exit()

    pygame.display.update()
    clock.tick(60)