import pygame

from src.utilities.debug import debug


class PlayerActionDispatcher:

    def __init__(self, create_weapon, remove_weapon, change_weapon):
        self._is_attacking = False
        self._attack_cooldown = 400
        self._attack_time = None

        self._can_switch_weapon = True
        self._switch_weapon_cooldown = 200
        self._switch_weapon_time = None

        self._status = "down"
        self._create_weapon = create_weapon
        self._remove_weapon = remove_weapon
        self._change_weapon = change_weapon

    def dispatch(self, direction):
        keys = self._get_input_action()

        if not self._is_attacking:

            if self._is_moving_up(keys):
                direction.y = -1
                self._status = "up"
            elif self._is_moving_down(keys):
                direction.y = 1
                self._status = "down"
            else:
                direction.y = 0

            if self._is_moving_right(keys):
                direction.x = 1
                self._status = "right"
            elif self._is_moving_left(keys):
                direction.x = -1
                self._status = "left"
            else:
                direction.x = 0

            if keys[pygame.K_SPACE]:
                self._is_attacking = True
                self._attack_time = pygame.time.get_ticks()
                self._create_weapon()

            if keys[pygame.K_LCTRL]:
                self._is_attacking = True
                self._attack_time = pygame.time.get_ticks()
                self._create_weapon()

            if keys[pygame.K_q] and self._can_switch_weapon:
                self._can_switch_weapon = False
                self._switch_weapon_time = pygame.time.get_ticks()
                self._change_weapon()

        if direction.x == 0 and direction.y == 0 and 'idle' not in self._status and 'attack' not in self._status:
            self._status = self._status + "_idle"

        if self._is_attacking:
            direction.x = 0
            direction.y = 0
            if 'attack' not in self._status:
                if 'idle' in self._status:
                    self._status = self._status.replace("_idle", "_attack")
                else:
                    self._status = self._status + "_attack"
        else:
            if 'attack' in self._status:
                self._status = self._status.replace("_attack", "")

        debug(f"Status: {self._status}", y=35)
        return direction

    def attack_cooldown(self):
        current_time = pygame.time.get_ticks()
        if self._is_attacking:
            if current_time - self._attack_time >= self._attack_cooldown:
                self._is_attacking = False
                self._remove_weapon()

    def weapon_switch_cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self._can_switch_weapon:
            if current_time - self._switch_weapon_time >= self._switch_weapon_time:
                self._can_switch_weapon = True

    def _get_input_action(self):
        return pygame.key.get_pressed()

    def _is_moving_left(self, keys):
        return keys[pygame.K_LEFT]

    def _is_moving_right(self, keys):
        return keys[pygame.K_RIGHT]

    def _is_moving_down(self, keys):
        return keys[pygame.K_DOWN]

    def _is_moving_up(self, keys):
        return keys[pygame.K_UP]

    def get_status(self):
        return self._status
