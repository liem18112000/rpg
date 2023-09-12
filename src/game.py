import pygame
import sys

from .configs.settings import *
from src.level.levels import Level


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME_TITLE)

        self._screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self._clock = pygame.time.Clock()
        self._is_running = True
        self._level = Level()

    def _initialize_screen(self):
        self._screen.fill("black")

    def _initialize_level(self):
        self._level.start()

    def run(self):
        while self._is_running:
            self._dispatch_event(pygame.event.get())
            self._initialize_screen()
            self._initialize_level()
            # debug("Debug")
            pygame.display.update()
            self._clock.tick(FPS)

    def _dispatch_event(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self._quit()

    def _quit(self):
        self._is_running = False
        pygame.quit()
        sys.exit()
