import pygame
from jobe.virtual.MowedPart import MowedPart
from jobe.virtual.Mower import Mower


class StopOver:
    """This class renders a fictitious lawn for simulation purposes"""

    def __init__(self):
        """This constructor will initialize the class"""
        pygame.init()

        # How big should the board be? Also set the tile size
        self._board_x_size = 512
        self._board_y_size = 512
        self._tile_size = 16

        # Set the window's icon
        pygame.display.set_icon(pygame.image.load("jobe/resources/Tree.png"))

        # Create the window and its title
        self._screen = pygame.display.set_mode(
            (self._board_x_size, self._board_y_size)
        )
        pygame.display.set_caption("Jobe Simulator")

        # Define the tree image, the mower sprite, and the lawn data path
        self._tree_image = pygame.image.load(
            "jobe/resources/Tree.png"
        ).convert()
        self._mower = Mower(
            pygame.image.load("jobe/resources/Mower.png").convert()
        )
        self._lawn_file_path = "jobe/resources/yard.dat"

        # Define our colors
        self._long_grass_color = pygame.Color(0, 135, 38, 255)
        self._short_grass_color = pygame.Color(0, 201, 57, 255)

        # Set up the sprite group for the mowed parts
        self._mowed_parts = pygame.sprite.Group()
        self._newly_mowed_parts = pygame.sprite.Group()

        # Load the yard file into memory
        self._load_yard_file()

    def _load_yard_file(self):
        """This private method will load the board from disk into memory"""
        self._yard_data = []

        # Open a handle to the lawn file, loop through each line
        with open(self._lawn_file_path, "r") as file:
            for line in file:
                new_line = []

                # Loop through each character in the line and append it
                for character in line:
                    new_line.append(character)

                # Append the new line to the yard data
                self._yard_data.append(new_line)

    def is_mower_hitting_mowed_grass(self):
        """This method will return if the mower is colliding with the mowed"""
        collisions = pygame.sprite.spritecollide(
            self._mower,
            self._mowed_parts,
            False
        )

        # Did any collisions occur?
        return len(collisions) > 0

    def draw_yard(self, mower_x, mower_y, mower_angle, first_time=False):
        """This method will render the current frame"""
        pygame.time.delay(10)

        # Do this initial rendering only on the first frame
        if first_time:

            # Render the un-mowed grass
            long_grass = pygame.Surface((512, 512))
            long_grass.fill(self._long_grass_color)
            self._screen.blit(long_grass, (0, 0))

            # Now, loop through the board and draw the trees and mowed parts
            current_x = 0
            current_y = 0
            for row in self._yard_data:
                for tile in row:
                    if first_time and tile == "T":
                        # Draw a tree
                        self._screen.blit(
                            self._tree_image,
                            (current_x, current_y)
                        )
                    if tile == "M":
                        # Add a new mowed part to the group
                        self._mowed_parts.add(MowedPart(
                            self._short_grass_color,
                            current_x,
                            current_y,
                            self._tile_size,
                            self._tile_size
                        ))
                    current_x += self._tile_size
                current_x = 0
                current_y += self._tile_size

        # Do this stuff every frame
        else:

            # Rotate the mower
            rotated_mower = self._mower.reposition_mower(
                mower_y,
                mower_x
            )

            # Have the mower cut the grass where it is presently
            mowed_position = self._mower.get_trail_spot(mower_angle)
            self._newly_mowed_parts.add(MowedPart(
                self._short_grass_color,
                mowed_position[1],
                mowed_position[0],
                rotated_mower.get_width(),
                rotated_mower.get_height()
            ))

            # Draw the mowed parts and the mower itself
            self._mowed_parts.draw(self._screen)
            self._newly_mowed_parts.draw(self._screen)
            self._screen.blit(rotated_mower, (mower_x, mower_y))

        # We're done! Display the buffer
        pygame.display.update()
