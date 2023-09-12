from src.utilities.debug import debug


class PlayerCollider:

    def on_vertical_collision(self, hit_box, direction, obstacle_sprites):
        collide_side = "NONE"
        for sprite in obstacle_sprites:
            if self._is_player_collide_with_obstacle(hit_box, sprite):
                if self._is_player_moving_down(direction):
                    hit_box.bottom = self._stop_player_on_obstacle_top_side(hit_box, sprite)
                    collide_side = "BOTTOM"
                if self._is_player_moving_up(direction):
                    hit_box.top = self._stop_player_on_obstacle_bottom_side(hit_box, sprite)
                    collide_side = "TOP"
                break
        debug(f"Collide vertical: {collide_side}", y=85)
        return hit_box

    def on_horizontal_collision(self, hit_box, direction, obstacle_sprites):
        collide_side = "NONE"
        for sprite in obstacle_sprites:
            if self._is_player_collide_with_obstacle(hit_box, sprite):
                if self._is_player_moving_right(direction):
                    hit_box.right = self._stop_player_on_obstacle_left_side(hit_box, sprite)
                    collide_side = "RIGHT"
                if self._is_player_moving_left(direction):
                    hit_box.left = self._stop_player_on_obstacle_right_side(hit_box, sprite)
                    collide_side = "LEFT"
                break
        debug(f"Collide horizontal: {collide_side}", y=110)
        return hit_box

    def _stop_player_on_obstacle_bottom_side(self, hit_box, sprite):
        hit_box.top = sprite.hit_box.bottom
        return hit_box.top

    def _stop_player_on_obstacle_top_side(self, hit_box, sprite):
        hit_box.bottom = sprite.hit_box.top
        return hit_box.bottom

    def _is_player_moving_up(self, direction):
        return direction.y < 0

    def _is_player_moving_down(self, direction):
        return direction.y > 0

    def _stop_player_on_obstacle_right_side(self, hit_box, sprite):
        hit_box.left = sprite.hit_box.right
        return hit_box.left

    def _is_player_moving_left(self, direction):
        return direction.x < 0

    def _stop_player_on_obstacle_left_side(self, hit_box, sprite):
        hit_box.right = sprite.hit_box.left
        return hit_box.right

    def _is_player_moving_right(self, direction):
        return direction.x > 0

    def _is_player_collide_with_obstacle(self, hit_box, sprite):
        return sprite.hit_box.colliderect(hit_box)
