import os.path

from src.utilities.layout import import_folder


class PlayerAnimation:
    def __init__(self):
        self._character_path = "./src/assess/player"
        self.animations = {
            "up": [], "down": [], "left": [], "right": [],
            "right_idle": [], "down_idle": [], "left_idle": [], "up_idle": [],
            "right_attack": [], "down_attack": [], "left_attack": [], "up_attack": [],
        }
        self.frame_index = 0
        self.animation_speed = 0.15
        for animation in self.animations.keys():
            full_path = os.path.join(self._character_path, animation)
            self.animations[animation] = import_folder(full_path)

    def animate(self, status):
        animation = self.animations[status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        return animation[int(self.frame_index)]
