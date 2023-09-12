import pygame

from src.configs.settings import HIT_BOX_INFLATE_X, HIT_BOX_INFLATE_Y, TILESIZE
from src.title.tile import Tile


class BoundaryTile(Tile):

    def __init__(self, position, groups, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(position, groups, surface)