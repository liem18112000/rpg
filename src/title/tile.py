import pygame

from src.configs.settings import ROCK_IMAGE_PATH, HIT_BOX_INFLATE_X, HIT_BOX_INFLATE_Y, TILESIZE


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_rect(topleft=position)
        self.hit_box = self.rect.inflate(HIT_BOX_INFLATE_X, HIT_BOX_INFLATE_Y)
        self.sprite_type = sprite_type


class ObjectTile(Tile):
    def __init__(self, position, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(position, groups, sprite_type, surface)
        self.rect = self.image.get_rect(topleft=(position[0],position[1] - TILESIZE))

