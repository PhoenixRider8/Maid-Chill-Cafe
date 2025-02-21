import pygame
import time

# Initialize Pygame
#pygame.init()

class Timer:
    def __init__(self, screen, font, x, y):
        self.screen = screen
        self.font = font
        self.x = x
        self.y = y
        self.total_seconds = 0  # Total time in seconds
        self.time_left = 0      # Time remaining in seconds
        self.start_time = None  # Time when the timer starts

    def set_time(self, minutes, seconds):
        """Set the timer to a specific time (in minutes and seconds)."""
        self.total_seconds = minutes * 60 + seconds
        self.time_left = self.total_seconds
        self.start_time = time.time()  # Start the timer from now

    def update(self):
        """Update the countdown time."""
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            remaining_time = self.total_seconds - int(elapsed_time)

            # If time is up, stop the timer at 0
            if remaining_time < 0:
                remaining_time = 0

            self.time_left = remaining_time

        # Convert remaining time to minutes and seconds
        minutes = self.time_left // 60
        seconds = self.time_left % 60

        # Display the time in mm:ss format
        time_str = f"{minutes:02}:{seconds:02}"
        text_surface = self.font.render(time_str, True, (255, 255, 255))
        self.screen.blit(text_surface, (self.x, self.y))

def main():
    # Set up the display
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Countdown Timer")

    # Font for the timer text
    font = pygame.font.Font(None, 74)

    # Create Timer instance
    timer = Timer(screen, font, 150, 100)

    # Set the time to 2 minutes and 30 seconds
    timer.set_time(2, 30)

    # Main loop
    running = True
    while running:
        screen.fill((0, 0, 0))  # Fill the screen with black
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and display the timer
        timer.update()

        # Update the screen
        pygame.display.flip()
        pygame.time.Clock().tick(30)  # Limit the frame rate to 30 FPS

    pygame.quit()
'''
if __name__ == "__main__":
    main()
'''
