import pygame

from src.configs.settings import DEBUG_MODE

pygame.init()
font = pygame.font.Font(None, 25)


def debug(info, y=10, x=10):
    if DEBUG_MODE:
        display_surface = pygame.display.get_surface()
        debug_surface = font.render(str(info), True, "White")
        debug_rect = debug_surface.get_rect(topleft=(x, y))
        display_surface.blit(debug_surface, debug_rect)
        next_debug_info_position = (x, y + 32)
