import pygame
from scripts.Constants.config import *

class Menu:
    def __init__(self, screen):
        # Store the screen and button images passed during initialization
        self.screen = screen

        #BUTTONS
        self.start_img = pygame.image.load(start_Button)
        self.quit_img = pygame.image.load(stop_Button)

        #WINDOW SCREEN
        self.window_screen = pygame.image.load(window_img)
        self.font = pygame.font.Font(FONT, 36)
        self.running = True

        # Define button positions (adjust them as needed)
        self.start_button_rect = self.start_img.get_rect(
            center=(self.screen.get_width() // 2 + 200, self.screen.get_height() // 2 + 20))
        self.quit_button_rect = self.quit_img.get_rect(
            center=(self.screen.get_width() // 2 + 200, self.screen.get_height() // 2 + 100))

    def event(self):
        # Event handler to handle user input (e.g., quitting, key presses, mouse clicks)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Stop the main loop if the user closes the window
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False  # Exit on Escape key
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    if self.start_button_rect.collidepoint(event.pos):
                        print("Start button clicked!")
                        # Call the function to start the game or change to the game screen
                        self.start_game()
                    elif self.quit_button_rect.collidepoint(event.pos):
                        print("Quit button clicked!")
                        self.running = False  # Quit the menu and the program

    def start_game(self):
        # This function will be called when the "Start" button is clicked
        # Here you can transition to the game screen or start the game logic
        print("Starting game...")
        self.running = False

    def main(self):
        # Main loop to continuously update the menu
        while self.running:
            self.event()  # Handle events like quitting, key presses, or mouse clicks

            # Clear the screen by filling it with a color (black)
            self.screen.fill((0, 0, 0))

            #Draw window image
            self.screen.blit(self.window_screen,(0,0))

            # Draw the buttons on the screen (drawing within rect
            self.screen.blit(self.start_img, self.start_button_rect)
            self.screen.blit(self.quit_img, self.quit_button_rect)

            # Update the screen
            pygame.display.flip()

            # Control the frame rate (60 FPS)
            pygame.time.Clock().tick(60)
