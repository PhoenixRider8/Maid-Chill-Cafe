from pygame import mixer
import pygame
from scripts.Constants.musicList import *
import sys


class Music:
    def __init__(self):
        try:
            mixer.init()  # Initialize the mixer
        except pygame.error as e:
            print("Error initializing pygame.mixer:", e)
            sys.exit(1)  # Exit if the mixer couldn't be initialized

        self.stopPlaying = False
        self.current_music = None  # Track current music

    def play(self, loop=True):
        """Play the current music. Optionally loop the music."""
        if self.current_music:
            mixer.music.set_volume(0.7)  # Set volume
            loops = -1 if loop else 0  # Loop indefinitely if True, or play once
            mixer.music.play(loops=loops)  # Play music with specified loops

    def pickMusic(self, name):
        """Select the music based on the name."""
        # Ensure that you are loading the correct music
        if name == 'dialogue':
            print("Loading dialogue music...")
            self._load_music(game1)
        elif name == 'mainMenu':
            print("Loading main menu music...")
            self._load_music(game3)
        elif name == 'game3':
            print("Loading game music...")
            self._load_music(game2)
        else:
            print(f"Error: Unknown music name '{name}'")

    def _load_music(self, music_file):
        """Load the specified music file."""
        try:
            mixer.music.load(music_file)
            self.current_music = music_file
        except pygame.error as e:
            print(f"Error loading music file {music_file}: {e}")
            self.current_music = None  # Reset the current music in case of an error

    def stop(self):
        """Stop the currently playing music."""
        if self.stopPlaying and self.current_music:
            mixer.music.stop()

    def toggle_stop(self):
        """Toggle the stop state."""
        self.stopPlaying = not self.stopPlaying
