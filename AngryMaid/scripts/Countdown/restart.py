import pygame
import pyautogui
import sys
import time

class RestartGame:
    def __init__(self):
        pygame.init()

        # Create a screen with the specified dimensions
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Restart PC Game")

        # Set up font
        self.font = pygame.font.SysFont("Arial", 40)

        # Background color
        self.bg_color = (0, 0, 0)

        # Main loop flag
        self.running = True

    def draw_text(self, text, color, y_offset):
        """Utility function to render and display text."""
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (self.screen.get_width() // 2 - text_surface.get_width() // 2, self.screen.get_height() // 2 + y_offset))

    def restart_pc(self):
        """Function to restart the PC using pyautogui."""
        try:
            print("Restarting PC...")
            # This will simulate a press of the Windows key and 'R' to open the Run dialog
            pyautogui.hotkey('win', 'r')
            time.sleep(0.5)  # Wait for the Run dialog to open
            # Type the restart command
            pyautogui.write('shutdown /r /t 0')  # The /r means restart, and /t 0 is for immediate restart
            pyautogui.press('enter')
        except Exception as e:
            print(f"Error while trying to restart PC: {e}")

    def main_loop(self):
        while self.running:
            self.screen.fill(self.bg_color)

            # Check events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Press "R" key to restart the PC
                        self.restart_pc()

            # Draw instructions
            self.draw_text("CYA!!!!", (255, 255, 255), -100)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

# Run the game
if __name__ == "__main__":
    game = RestartGame()
    game.main_loop()
