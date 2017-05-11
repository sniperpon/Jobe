import pygame


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

        # Define our images and paths
        self._mower = pygame.image.load("jobe/resources/Arrow.png").convert()
        self._tree = pygame.image.load("jobe/resources/Tree.png").convert()
        self._lawn_file_path = "jobe/resources/yard.dat"

        # Define our colors
        self._long_grass_color = pygame.Color(0, 135, 38, 255)
        self._short_grass_color = pygame.Color(0, 201, 57, 255)

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

    def draw_yard(self, mower_x, mower_y, mower_angle):
        """This method will render the current frame"""
        pygame.time.delay(10)

        # Render the short grass underneath
        short_grass = pygame.Surface((512, 512))
        short_grass.fill(self._short_grass_color)
        self._screen.blit(short_grass, (0, 0))

        # Render the long grass over the top
        long_grass = pygame.Surface((512, 512))
        long_grass.fill(self._long_grass_color)
        self._screen.blit(long_grass, (0, 0))

        # Rotate the mower and render it
        rotated_mower = pygame.transform.rotate(self._mower, mower_angle)
        self._screen.blit(rotated_mower, (mower_x, mower_y))

        # Now, loop through the board and draw the trees
        current_x = 0
        current_y = 0
        for row in self._yard_data:
            for tile in row:
                if tile == "T":
                    self._screen.blit(self._tree, (current_x, current_y))
                current_x += self._tile_size
            current_x = 0
            current_y += self._tile_size

        # Display the buffer
        pygame.display.update()
