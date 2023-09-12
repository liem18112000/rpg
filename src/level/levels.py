from random import choice

import pygame

from src.camera import YSortCameraGroup
from src.configs.settings import TILESIZE, OBJECT_FOLDER, GRASS_FOLDER, OBJECT_MAP, GRASS_MAP, BOUNDARY_MAP
from src.level.builder import LevelMapBuilder
from src.player.player import Player
from src.title.tile import Tile, ObjectTile
from src.utilities.debug import debug
from src.utilities.layout import import_layout, import_folder
from src.weapon import Weapon


class Level:
    def __init__(self):
        self._visible_sprites = YSortCameraGroup()
        self._obstacle_sprites = pygame.sprite.Group()
        self._display_surface = pygame.display.get_surface()
        self._map_builder = LevelMapBuilder({
            "boundary": import_layout(BOUNDARY_MAP),
            "grass": import_layout(GRASS_MAP),
            "object": import_layout(OBJECT_MAP)
        })
        self._current_weapon = None
        self._build_map()

    def _build_map(self):
        graphics = {
            "grass": import_folder(GRASS_FOLDER),
            "objects": import_folder(OBJECT_FOLDER)
        }
        self._map_builder.build({
            "boundary": lambda position, value: Tile(position, [self._obstacle_sprites], "invisible"),
            "grass": lambda position, value: Tile(position, [self._visible_sprites, self._obstacle_sprites],
                                                  "grass", choice(graphics["grass"])),
            "object": lambda position, value: ObjectTile(position, [self._visible_sprites, self._obstacle_sprites],
                                                         "object", graphics['objects'][int(value)])
        })
        self._player = Player((2000, 1400), [self._visible_sprites],
                              self._obstacle_sprites, self._build_weapon, self._remove_weapon)

    def _build_weapon(self):
        self._current_weapon = Weapon(self._player, [self._visible_sprites])

    def _remove_weapon(self):
        if self._current_weapon:
            self._current_weapon.kill()
        self._current_weapon = None

    def start(self):
        self._visible_sprites.custom_draw(self._player)
        self._visible_sprites.update()
        debug(f"Player position: [{self._player.rect.centerx}, {self._player.rect.centery}]")
