import pygame
from scripts.Constants.config import cafe_img  # Assuming cafe_img is the file path
from scripts.dialogueSystem.dialogueSys import DialogueSystem
from scripts.Constants.config import FONT
from PIL import Image, ImageFilter


class Dialogue:
    def __init__(self, screen):
        # Store the screen passed during initialization
        self.screen = screen

        # Load the image using PIL (Pillow) and apply a blur filter
        self.cafeImg = pygame.image.load(cafe_img)

        # Convert the Pygame surface to a PIL Image object to apply blur
        pil_image = Image.open(cafe_img)
        self.blurred_image = pil_image.filter(ImageFilter.GaussianBlur(radius=5))  # You can adjust the radius

        # Convert the blurred PIL image back to a Pygame surface
        self.blurred_image = pygame.image.fromstring(self.blurred_image.tobytes(), self.blurred_image.size,
                                                     self.blurred_image.mode)

        self.font = pygame.font.Font(FONT, 32)  # Set font
        self.dialogueSys = DialogueSystem(self.screen, self.font)
        self.setDialogue1()
        self.counter = 0

        # Create the dialogue box surface with transparency (0.8 alpha)
        self.dialogue_box = pygame.Surface((self.screen.get_width(), 150))  # Adjust size as needed
        self.dialogue_box.fill((0, 0, 0))  # Fill with black
        self.dialogue_box.set_alpha(204)  # Set alpha to 0.8 (204 out of 255)

        self.spriteList = [
            pygame.image.load('assets/maidFull/maidFull3.png'),
            pygame.image.load('assets/maidFull/maidFull2.png'),
            pygame.image.load('assets/maidFull/maidFull2.png'),
            pygame.image.load('assets/maidFull/maidFull4.png'),
            pygame.image.load('assets/maidFull/maidFull5.png'),
            pygame.image.load('assets/maidFull/maidFull2.png')
        ]

        self.last_update_time = pygame.time.get_ticks()  # Get current time in milliseconds
        self.sprite_change_interval = 1000  # 1000 milliseconds = 1 second
        self.current_sprite = 0  # Start with the first sprite

    def setDialogue1(self):
        """Set up initial dialogues."""
        self.dialogueSys.add_dialogue("Clara", "Welcome Master!  ")
        self.dialogueSys.add_dialogue("Clara", "My name's Clara ")
        self.dialogueSys.add_dialogue("Clara", "Welcome to the Maid Cafe")
        self.dialogueSys.add_dialogue("Clara", "I will be on your service! ")
        self.dialogueSys.add_dialogue("Clara", "Let's play a mini-game")
        self.dialogueSys.add_dialogue("Clara", "Capture all my stickers for a special bonus :3")

    def run(self):
        # Run the game loop
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Clear the screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("Space bar pressed!")
                        if self.counter >= len(self.dialogueSys.dialogues):
                            running = False
                        else:
                            self.dialogueSys.display_next_dialogue()  # Display next dialogue
                            self.counter += 1

            # Blit the blurred background at position (0, 0)
            self.screen.blit(self.blurred_image, (0, 0))

            # Blit the transparent dialogue box over the screen
            self.screen.blit(self.dialogue_box, (0, self.screen.get_height() - 150))  # Adjust position as needed

            # Sync sprite based on time
            self.update_sprite()

            # Update and draw the dialogue text
            self.dialogueSys.update()

            # Update the display
            pygame.display.update()

        # Quit the game when the loop ends
        pygame.quit()

    def update_sprite(self):
        """Update the sprite every 1 second."""
        current_time = pygame.time.get_ticks()  # Get the current time in milliseconds

        # Check if 1 second (1000 milliseconds) has passed
        if current_time - self.last_update_time >= self.sprite_change_interval:
            # Update sprite to the next one
            self.current_sprite = (self.current_sprite + 1) % len(self.spriteList)  # Loop back to 0 if out of range
            self.last_update_time = current_time  # Update the last update time

        # Blit the current sprite
        self.screen.blit(self.spriteList[self.current_sprite], (0, 20))  # Draw the current sprite

