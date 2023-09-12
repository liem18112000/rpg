import pygame

from src.configs.settings import GROUND_IMAGE


class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self._display_surface = pygame.display.get_surface()
        self._offset = pygame.math.Vector2()
        self._half_width = self._display_surface.get_size()[0] // 2
        self._half_height = self._display_surface.get_size()[1] // 2

        self._floor_surface = pygame.image.load(GROUND_IMAGE).convert()
        self._floor_rect = self._floor_surface.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self._update_offset(player)

        floor_offset_position = self._floor_rect.topleft - self._offset
        self._display_surface.blit(self._floor_surface, floor_offset_position)

        for sprite in sorted(self.sprites(), key=lambda s: s.rect.centery):
            offset_position = sprite.rect.topleft - self._offset
            self._display_surface.blit(sprite.image, offset_position)

    def _update_offset(self, player):
        self._offset.x = player.rect.centerx - self._half_width
        self._offset.y = player.rect.centery - self._half_height
