import pygame
import os

# Initialize pygame
pygame.init()

# Set the window position (x, y)
window_pos = (200, 150)  # Set your desired position

# Set the environment variable before creating the window
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{window_pos[0]},{window_pos[1]}"

# Create the window with specific dimensions
screen = pygame.display.set_mode((800, 600))

# Title for the window
pygame.display.set_caption("Window at Specific Position")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
