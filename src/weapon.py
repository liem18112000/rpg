import pygame.sprite


class Weapon(pygame.sprite.Sprite):

    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.get_status().split("_")[0]
        self._name = player.get_weapon_name()
        self._attribute = player.get_weapon_attribute()

        full_path = f"./src/assess/weapons/{self._name}/{direction}.png"
        self.image = pygame.image.load(full_path).convert_alpha()

        if direction == "right":
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 16))
        elif direction == "left":
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))
        elif direction == "down":
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(0, 16))
        else:
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(0, 16))

    def get_name(self):
        return self._name

    def get_attribute(self):
        return self._attribute
