import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_SIZE = (800, 600)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake properties
SNAKE_SIZE = 10
snake_positions = [(100, 100), (90, 100), (80, 100)]
snake_direction = "right"

# Food properties
food_position = (random.randrange(1, (WINDOW_SIZE[0] // SNAKE_SIZE)) * SNAKE_SIZE,
                 random.randrange(1, (WINDOW_SIZE[1] // SNAKE_SIZE)) * SNAKE_SIZE)
food_spawn = True

# Game variables
score = 0
clock = pygame.time.Clock()
SNAKE_SPEED = 8  # Adjust this value to control the snake's speed

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"
            elif event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"

    # Move the snake continuously
    new_head = list(snake_positions[0])
    if snake_direction == "left":
        new_head[0] -= SNAKE_SIZE
    elif snake_direction == "right":
        new_head[0] += SNAKE_SIZE
    elif snake_direction == "up":
        new_head[1] -= SNAKE_SIZE
    elif snake_direction == "down":
        new_head[1] += SNAKE_SIZE
    snake_positions.insert(0, tuple(new_head))

    # Check for food
    if snake_positions[0] == food_position:
        food_spawn = False
        score += 1
    else:
        snake_positions.pop()

    # Spawn new food
    if not food_spawn:
        food_position = (random.randrange(1, (WINDOW_SIZE[0] // SNAKE_SIZE)) * SNAKE_SIZE,
                         random.randrange(1, (WINDOW_SIZE[1] // SNAKE_SIZE)) * SNAKE_SIZE)
        food_spawn = True

    # Check for window border collision
    head_x, head_y = snake_positions[0]
    if head_x < 0 or head_x >= WINDOW_SIZE[0] or head_y < 0 or head_y >= WINDOW_SIZE[1]:
        # Reset the game
        snake_positions = [(100, 100), (90, 100), (80, 100)]
        snake_direction = "right"
        score = 0

    # Clear the window
    window.fill(BLACK)

    # Draw the snake
    for position in snake_positions:
        pygame.draw.rect(window, GREEN, (position[0], position[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw the food
    pygame.draw.rect(window, RED, (food_position[0], food_position[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw the score
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Control the snake's speed
    clock.tick(SNAKE_SPEED)