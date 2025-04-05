import pygame
from constants import *
from circleshape import CircleShape
from explosion import Explosion

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

class FastShot(Shot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = SHOT_RADIUS * 0.7
        self.velocity = pygame.Vector2(0, 0)
        self.speed_multiplier = 3

    def update(self, dt):
        self.position += self.velocity * dt * self.speed_multiplier
    
class SpreadShot(Shot):
    def __init__(self, x, y, angle_offset):
        super().__init__(x, y)
        self.angle_offset = angle_offset

    def set_velocity(self, base_velocity):
        self.velocity = base_velocity.rotate(self.angle_offset)

class BigShot(Shot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = SHOT_RADIUS * 3
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
