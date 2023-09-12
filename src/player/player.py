import pygame

from src.configs.settings import PLAYER_IMAGE_PATH, MOVE_SPEED, HIT_BOX_INFLATE_Y
from src.configs.weapons import WEAPONS
from src.player.animate import PlayerAnimation
from src.player.collider import PlayerCollider
from src.player.dispatcher import PlayerActionDispatcher
from src.utilities.debug import debug


class Player(pygame.sprite.Sprite):

    def __init__(self, position, groups, obstacle_sprites, create_weapon, remove_weapon):
        super().__init__(groups)
        self.image = pygame.image.load(PLAYER_IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
        self.direction = pygame.math.Vector2()
        self.obstacle_sprites = obstacle_sprites
        self.hit_box = self.rect.inflate(-16, HIT_BOX_INFLATE_Y * 2.5)

        self.weapon_index = 0
        self.weapon_name = list(WEAPONS.keys())[self.weapon_index]
        self.weapon_attribute = WEAPONS[self.weapon_name]

        self._dispatcher = PlayerActionDispatcher(create_weapon, remove_weapon, self.change_weapon)
        self._collider = PlayerCollider()
        self._animator = PlayerAnimation()

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hit_box.x += self.direction.x * speed
        self.hit_box = self._collider.on_horizontal_collision(self.hit_box, self.direction, self.obstacle_sprites)
        self.hit_box.y += self.direction.y * speed
        self.hit_box = self._collider.on_vertical_collision(self.hit_box, self.direction, self.obstacle_sprites)
        self.rect.center = self.hit_box.center

    def animate(self):
        status = self.get_status()
        self.image = self._animator.animate(status)
        self.rect = self.image.get_rect(center=self.hit_box.center)

    def get_status(self):
        return self._dispatcher.get_status()

    def update(self):
        self.direction = self._dispatcher.dispatch(self.direction)
        self._dispatcher.attack_cooldown()
        self._dispatcher.weapon_switch_cooldown()
        self.animate()
        self.move(MOVE_SPEED)
        debug(f"Weapon: {self.weapon_name}", y=60)

    def get_weapon_name(self):
        return self.weapon_name

    def change_weapon(self):
        if self.weapon_index < len(list(WEAPONS.keys())) - 1:
            self.weapon_index += 1
        else:
            self.weapon_index = 0
        self.weapon_name = list(WEAPONS.keys())[self.weapon_index]
        self.weapon_attribute = WEAPONS[self.weapon_name]

    def get_weapon_attribute(self):
        return self.weapon_attribute


