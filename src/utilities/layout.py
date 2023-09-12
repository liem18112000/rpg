import os.path
from csv import reader
from os import walk

import pygame


def import_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    surface_list = []
    for root, folder, files in walk(path):
        for file in files:
            full_path = os.path.join(path, file)
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
    return surface_list
