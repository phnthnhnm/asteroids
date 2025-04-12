import pygame
from constants import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # Wrap around the screen
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT

    def collide(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius
