import sys
import pygame
from jobe.simulator.Mower import Mower
from jobe.simulator.Grass import Grass
from jobe.simulator.Grass import GrassType
from jobe.simulator.Tree import Tree


class Simulator:
    """This is the main driver class for the simulator"""

    def __init__(self, input_handler):
        """Initialize pygame"""
        pygame.init()
        self._clock = pygame.time.Clock()
        self._input_handler = input_handler

        # How big should the board be? Also set the tile size
        board_x_tiles = 32
        board_y_tiles = 32
        self._tile_size = 16
        self._yard_data = []

        # Set the window's icon, get its info object, and set the file path
        pygame.display.set_icon(pygame.image.load("jobe/resources/Tree.png"))
        info = pygame.display.Info()
        self._lawn_file_path = "jobe/resources/yard.dat"

        # Create the window and its title
        self._screen = pygame.display.set_mode(
            (board_x_tiles * self._tile_size, board_y_tiles * self._tile_size)
        )
        pygame.display.set_caption("Jobe Simulator")

        # Prepare our game objects
        self._grasses = pygame.sprite.Group()
        self._grasses.add(Grass(
            0, 0, info.current_w, info.current_h, GrassType.Tall
        ))
        self._obstacles = pygame.sprite.Group()
        self._mowers = pygame.sprite.Group()
        self._mowers.add(Mower(256, 256, 270, 1))

        # Load the board objects
        self._load_file()

    def run(self):
        """This method contains the main game loop"""
        while 1:
            # Regulate the frame rate to 60 frames per second
            self._clock.tick(60)

            # Update object statuses based on input
            self._process_input()

            # Update all of the sprites
            self._grasses.update()
            self._obstacles.update()
            self._mowers.update(self._obstacles)

            # Draw all of the sprites to the back buffer
            self._grasses.draw(self._screen)
            self._obstacles.draw(self._screen)
            self._mowers.draw(self._screen)

            # Flip the front and back buffers
            pygame.display.update()

    def _process_input(self):
        """This method will return the input that the user has inputted"""
        if self._input_handler.turn_left():
            self._mowers.sprites()[0].rotate_ccw()
        if self._input_handler.turn_right():
            self._mowers.sprites()[0].rotate_cw()
        if self._input_handler.move_forward():
            self._mowers.sprites()[0].forward()
        if self._input_handler.move_backwards():
            self._mowers.sprites()[0].backwards()

        # Also read pygame's events to look for typed input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Escape quits
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _load_file(self):
        """This method will load a file from disk, and add sprites to groups"""
        current_left = 8
        current_top = 8

        # Open a handle to the lawn file, loop through each line
        with open(self._lawn_file_path, "r") as file:
            for line in file:
                new_line = []

                # Loop through each character in the line and append it
                for character in line:
                    new_line.append(character)

                    # If the character is a tree, then add one to the group
                    if character == "T":
                        self._obstacles.add(Tree(current_left, current_top))

                    # If the character is mowed grass, then add to the group
                    if character == "M":
                        self._obstacles.add(Grass(
                            current_left,
                            current_top,
                            self._tile_size,
                            self._tile_size,
                            GrassType.Short
                        ))

                    # We're done with a character
                    current_left += self._tile_size

                # We're done with a line
                current_left = 8
                current_top += self._tile_size

                # Append the new line to the yard data
                self._yard_data.append(new_line)
