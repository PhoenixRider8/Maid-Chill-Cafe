import pygame
import random
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSPARENT_GRAY = (128, 128, 128, 128)  # 50% transparency

# Load the image
image_path = "assets/draw/apple.png"  # Replace with your image path
image = pygame.image.load(image_path)

# Scale image to fit the screen
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trace the Image")

# Player drawing surface
draw_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

# Game over flag
game_over = False


# Function to check if the player's drawing is 50% accurate
def check_accuracy(image, draw_surface):
    # Convert both image and draw_surface to grayscale for comparison
    image_array = pygame.surfarray.array3d(image)
    draw_array = pygame.surfarray.array3d(draw_surface)

    # Convert to binary images (simplified version)
    image_binary = np.mean(image_array, axis=2) < 128  # Darker pixels are part of the shape
    draw_binary = np.mean(draw_array, axis=2) < 128

    # Calculate accuracy (intersection over union)
    intersection = np.sum(image_binary & draw_binary)
    union = np.sum(image_binary | draw_binary)

    if union == 0:
        return 1.0  # No shapes in either image
    accuracy = intersection / union
    return accuracy


# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Drawing phase
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            pygame.draw.circle(draw_surface, BLACK, (x, y), 5)

        # Check accuracy
        accuracy = check_accuracy(image, draw_surface)
        if accuracy < 0.5:  # If accuracy is less than 50%
            game_over = True

        # Clear the screen and draw the transparent image
        screen.fill(WHITE)
        transparent_image = image.copy()
        transparent_image.fill(TRANSPARENT_GRAY, special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(transparent_image, (0, 0))
        screen.blit(draw_surface, (0, 0))  # Draw player's tracing on top

        # Display the current accuracy
        font = pygame.font.SysFont(None, 36)
        accuracy_text = font.render(f"Accuracy: {accuracy * 100:.1f}%", True, BLACK)
        screen.blit(accuracy_text, (10, 10))

        # If game over, show a message
        if game_over:
            game_over_text = font.render("Game Over! You did not trace accurately.", True, BLACK)
            screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2))

    pygame.display.update()
    clock.tick(FPS)
