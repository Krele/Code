import pygame
from spritesheet_functions import SpriteSheet
from random import randrange

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

ground = []
for i in range(5):
    ground.append([64*i,128,64,64])

decor_dark = []
for i in range(5):
    decor_dark.append([64*i,0,64,64])

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet('resources/My_first_sprite_sheet.png')
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()



