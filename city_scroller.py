"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x_point,self.y_point, self.width, self.height))
        """
        uses pygame and the global screen variable to draw the building on the screen
        the given rect is the area of a rectangle
        """

    def move(self, speed):
        self.x_point += speed
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """



class Scroller(object):

    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.buildings_list = []
        self.create_buildings()

    def create_buildings(self):
        combined_width = 0
        print('combined_width')
        while combined_width <= self.width:
            self.create_building(combined_width)
            combined_width += self.buildings_list[-1].width

    def create_building(self, x_location, width = random.randint(10, 60)):
        building1 = Building(x_location, 300, width, random.randint(-200, -80), WHITE)

        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """
        self.buildings_list.append(building1)

    def draw_buildings(self):
        self.buildings_list[0].color = RED
        self.buildings_list[-1].color = GREY

        for current_building in self.buildings_list:
            current_building.draw()
        # for each building in buildings_list draw it on the screen
        """
        This calls the draw method on each building.
        """

    def move_buildings(self):
        for current_building in self.buildings_list:
            current_building.move(2)

        # last_building = self.buildings_list[]
        # first_building = self.buildings_list[]

        if self.buildings_list[-1].x_point > SCREEN_WIDTH:
            self.buildings_list.remove(self.buildings_list[-1])
        if self.buildings_list[0].x_point > 0:
            width = random.randint(10, 60)
            x_location = self.buildings_list[0].x_point - width
            building = Building(x_location, 300, width, random.randint(-200, -80), WHITE)
            self.buildings_list.insert(0, building)

        # if last building's x coordinate is greater than 800, then building should be deleted
        #if first building's x coordinate is greater than 0, add a building

        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """

        class Player(pygame.sprite.Sprite):
            def __init__(self, height, color):
                pygame.sprite.Sprite.__init__(self)


FRONT_SCROLLER_COLOR = RED
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = GREEN

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

# back_scroller.create_buildings()
# front_scroller.create_buildings()
# middle_scroller.create_buildings()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    # back_scroller.draw_buildings()
    # back_scroller.move_buildings()
    # middle_scroller.draw_buildings()
    # middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE

