from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        