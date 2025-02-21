import pygame
import random
from scripts.Countdown.restart import RestartGame
from scripts.Music.musicPlayer import Music
mS1 = Music()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game settings
donut_img = pygame.image.load('assets/draw/donutScreen.png')
MAID_IMAGE_PATHS = [
    'assets/stickers/maid1.png',  # Replace with your own image paths
    'assets/stickers/maid2.png',
    'assets/stickers/maid3.png',
    'assets/stickers/maid4.png',
    'assets/stickers/maid5.png',
]
BOMB_IMAGE_PATH = 'assets/ui/icons/bomb.png'  # Replace with your own image path

class FallingGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Maid Falling Game")
        pygame_icon = pygame.image.load('assets/ui/icons/icon.png')
        pygame.display.set_icon(pygame_icon)
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.res = RestartGame()

        mS1.pickMusic("game3")
        mS1.play()

        # Load images with their original resolution (228x152)
        self.maid_images = [pygame.image.load(path) for path in MAID_IMAGE_PATHS]
        self.bomb_image = pygame.image.load(BOMB_IMAGE_PATH)

        # Scale images by 80% (0.8) for the falling effect
        self.maid_images = [pygame.transform.scale(img, (int(228 * 0.8), int(152 * 0.8))) for img in self.maid_images]
        self.bomb_image = pygame.transform.scale(self.bomb_image, (int(50 * 0.8), int(50 * 0.8)))

        # List for maids and bombs
        self.maids = []
        self.bombs = []
        self.spawn_bombs(10)  # Spawn 10 bombs

        # Maid spawn timing
        self.last_spawn_time = pygame.time.get_ticks()  # Time when the last maid spawn happened
        self.maid_spawn_interval = 5000  # 5 seconds (in milliseconds)
        self.fall_speed = 1.5  # Adjusted fall speed for the larger images

    def spawn_bombs(self, count):
        """Spawn the specified number of bombs at random positions."""
        for _ in range(count):
            bomb_x = random.randint(0, SCREEN_WIDTH - 40)  # Adjusted for bomb size (scaled to 40x40)
            bomb_y = random.randint(-200, -50)  # Spawn off the top of the screen
            self.bombs.append([bomb_x, bomb_y])

    def spawn_maids(self):
        """Randomly spawn 1 to 3 maids every 5 seconds with random images."""
        current_time = pygame.time.get_ticks()  # Get current time in milliseconds
        if current_time - self.last_spawn_time >= self.maid_spawn_interval:
            # If 5 seconds have passed, spawn 1 to 3 maids
            num_maids = random.randint(1, 3)
            for _ in range(num_maids):
                maid_x = random.randint(100, 700)  # Adjust x position for 80% size
                maid_y = -int(152 * 0.8)  # Start above the screen (scaled height)
                maid_image = random.choice(self.maid_images)  # Randomly choose a maid image
                self.maids.append([maid_x, maid_y, maid_image, 0, 1])  # Add maid with image, rotation angle (0), and direction (1 for increasing)

            # Update the last spawn time to current time
            self.last_spawn_time = current_time

    def reset_game(self):
        """Reset the game to initial state."""
        self.maids = []  # Clear the maids list
        self.bombs = []  # Clear the bombs list
        self.spawn_bombs(10)  # Spawn 10 bombs again
        self.fall_speed = 1.5  # Reset fall speed
        self.game_over = False

    def draw(self):
        """Draw everything on the screen."""
        self.screen.fill(WHITE)
        self.screen.blit(donut_img,(0,0))
        # Draw maids with rotation effect
        for maid in self.maids:
            # Rotate the image to the current angle
            rotated_image = pygame.transform.rotate(maid[2], maid[3])
            # Calculate the new position to keep the image centered
            new_rect = rotated_image.get_rect(center=(maid[0] + int(228 * 0.8) // 2, maid[1] + int(152 * 0.8) // 2))
            self.screen.blit(rotated_image, new_rect.topleft)

            # Adjust rotation direction: increasing (1) or decreasing (-1)
            if maid[3] >= 15:  # If rotation hits 15 degrees, reverse direction
                maid[4] = -1
            elif maid[3] <= 0:  # If rotation hits 0 degrees, reverse direction
                maid[4] = 1

            # Apply the rotation change based on direction
            maid[3] += 0.1 * maid[4]  # Slowly increase or decrease the angle

        # Draw bombs
        for bomb in self.bombs:
            self.screen.blit(self.bomb_image, (bomb[0], bomb[1]))

        # Game Over message
        if self.game_over:
            font = pygame.font.SysFont(None, 55)
            game_over_text = font.render("Game Over! Click to Restart", True, GREEN)
            self.screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2))

            self.res.main_loop()

        pygame.display.flip()

    def handle_events(self):
        """Handle user input and events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if any maid is clicked
                for maid in self.maids:
                    if (maid[0] <= mouse_x <= maid[0] + int(228 * 0.8)) and (maid[1] <= mouse_y <= maid[1] + int(152 * 0.8)):
                        self.maids.remove(maid)  # Remove clicked maid
                        break

                # Check for bomb click
                for bomb in self.bombs:
                    if (bomb[0] <= mouse_x <= bomb[0] + 40) and (bomb[1] <= mouse_y <= bomb[1] + 40):  # 40x40 for bomb
                        self.game_over = True  # Bomb clicked, game over
            elif event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
                # Restart game on click after Game Over
                self.reset_game()

    def update(self):
        """Update game state."""
        if not self.game_over:
            # Spawn maids every 5 seconds
            self.spawn_maids()

            # Move maids down
            for maid in self.maids:
                maid[1] += self.fall_speed

            # Move bombs down
            for bomb in self.bombs:
                bomb[1] += self.fall_speed

            # Check if any maid or bomb falls off the screen
            for maid in self.maids:
                if maid[1] > SCREEN_HEIGHT:
                    self.game_over = True  # Maid falls off the screen

            # Reset bombs that fall off the screen and spawn them at the top
            for bomb in self.bombs:
                if bomb[1] > SCREEN_HEIGHT:
                    bomb[1] = random.randint(-200, -50)  # Reset bomb to spawn off-screen
                    bomb[0] = random.randint(0, SCREEN_WIDTH - 40)  # Randomize bomb position

    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # Frame rate 60 FPS

        pygame.quit()


if __name__ == "__main__":
    game = FallingGame()
    game.run()
