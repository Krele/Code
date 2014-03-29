import pygame

from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite


class World(pygame.sprite.Sprite):
  def __init__(self,sprite_sheet_data):
    pygame.sprite.Sprite.__init__(self)
    sprite_sheet = SpriteSheet('My_first_sprite_sheet.png')
    self.image = sprite_sheet.get_image(sprite_sheet_data[0])

    self.rect = self.image.get_rect()
