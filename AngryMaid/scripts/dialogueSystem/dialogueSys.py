import pygame

import pygame
from scripts.Constants.config import FONT

class DialogueSystem:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font  # Default font
        self.dialogues = []  # List of dialogues
        self.current_dialogue = 0  # Track the current dialogue index
        self.is_displaying = False  # Whether dialogue is currently being shown
        self.text_surface = None  # Surface to hold the rendered dialogue text

    def add_dialogue(self, speaker, text):
        """Add a new dialogue to the list"""
        self.dialogues.append({"speaker": speaker, "text": text})

    def display_next_dialogue(self):
        """Displays the next dialogue, or ends the dialogue sequence"""
        if self.current_dialogue < len(self.dialogues):
            dialogue = self.dialogues[self.current_dialogue]
            text = f"{dialogue['speaker']}: {dialogue['text']}"
            self.text_surface = self.font.render(text, True, (255, 255, 255))
            self.current_dialogue += 1
        else:
            self.is_displaying = False  # End the dialogue when all are displayed

    def start_dialogue(self):
        """Start displaying the first dialogue"""
        if self.dialogues:
            self.is_displaying = True
            self.current_dialogue = 0
            self.display_next_dialogue()

    def update(self):
        """Update the dialogue system, rendering the text to the screen"""
        if self.is_displaying:
            # Render the current dialogue text if available
            if self.text_surface:
                # Display the text on the bottom center of the screen
                text_rect = self.text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 50))
                self.screen.blit(self.text_surface, text_rect)

            # Check for user input to advance the dialogue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Space bar advances dialogue
                        self.display_next_dialogue()

            pygame.display.flip()  # Update the screen

    def change_font_size(self, new_size):
        """Change the font size dynamically"""
        self.font = pygame.font.Font(FONT, new_size)  # Update the font with the new size


# Example of usage:
'''
def main():
    dialogue_system = DialogueSystem(screen, font)

    # Add some dialogues
    dialogue_system.add_dialogue("Hero", "Hello there!")
    dialogue_system.add_dialogue("Villager", "Greetings, traveler.")
    dialogue_system.add_dialogue("Hero", "I need some information.")
    dialogue_system.add_dialogue("Villager", "What do you seek?")

    # Start the dialogue
    dialogue_system.start_dialogue()

    # Main game loop
    running = True
    while running:
        dialogue_system.update()

        # Exit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.time.wait(50)  # Small delay to avoid max CPU usage

    pygame.quit()

if __name__ == "__main__":
    main()
    pass

'''