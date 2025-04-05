import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.lifetime = 0.5  # seconds
        self.timer = self.lifetime

    def draw(self, screen):
        alpha = int((self.timer / self.lifetime) * 255)
        color = (255, 255, 255, alpha)
        surface = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surface, color, (self.radius, self.radius), self.radius)
        screen.blit(surface, (self.position.x - self.radius, self.position.y - self.radius))

    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.kill()
