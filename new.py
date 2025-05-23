# simple_game.py
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 200, 255)
BLOCK_COLOR = (255, 50, 50)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Block settings
block_size = 50
block_x = random.randint(0, WIDTH - block_size)
block_y = -block_size
block_speed = 5

clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Move block
    block_y += block_speed
    if block_y > HEIGHT:
        block_y = -block_size
        block_x = random.randint(0, WIDTH - block_size)
        score += 1

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    block_rect = pygame.Rect(block_x, block_y, block_size, block_size)
    if player_rect.colliderect(block_rect):
        running = False

    # Draw player and block
    pygame.draw.rect(screen, PLAYER_COLOR, player_rect)
    pygame.draw.rect(screen, BLOCK_COLOR, block_rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Game Over
screen.fill(WHITE)
game_over_text = font.render("Game Over!", True, (255,0,0))
score_text = font.render(f"Final Score: {score}", True, (0,0,0))
screen.blit(game_over_text, (WIDTH//2 - 80, HEIGHT//2 - 40))
screen.blit(score_text, (WIDTH//2 - 90, HEIGHT//2))
pygame.display.flip()
pygame.time.wait(2000)
pygame.quit()
sys.exit()