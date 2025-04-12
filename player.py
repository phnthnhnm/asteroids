import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot, FastShot, SpreadShot, BigShot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.acceleration = pygame.Vector2(0, 0)
        self.weapon_type = "default"
        self.q_key_pressed = False
        self.bigshot_cooldown = (
            PLAYER_SHOOT_COOLDOWN * 2
        )  # Slower fire rate for BigShot

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.acceleration += forward * PLAYER_ACCELERATION * dt
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

    def switch_weapon(self):
        if self.weapon_type == "default":
            self.weapon_type = "fast"
        elif self.weapon_type == "fast":
            self.weapon_type = "spread"
        elif self.weapon_type == "spread":
            self.weapon_type = "big"
        else:
            self.weapon_type = "default"

    def shoot(self, dt):
        if self.timer <= 0:
            if self.weapon_type == "big":
                self.timer = self.bigshot_cooldown
            else:
                self.timer = PLAYER_SHOOT_COOLDOWN

            forward = pygame.Vector2(0, 1).rotate(self.rotation)

            if self.weapon_type == "default":
                shot = Shot(
                    self.position.x + forward.x * self.radius,
                    self.position.y + forward.y * self.radius,
                )
                shot.velocity = forward * PLAYER_SHOOT_SPEED
                return shot

            elif self.weapon_type == "fast":
                shot = FastShot(
                    self.position.x + forward.x * self.radius,
                    self.position.y + forward.y * self.radius,
                )
                shot.velocity = forward * PLAYER_SHOOT_SPEED
                return shot

            elif self.weapon_type == "spread":
                spread_shots = []
                for angle in [-15, 0, 15]:
                    spread_shot = SpreadShot(
                        self.position.x + forward.x * self.radius,
                        self.position.y + forward.y * self.radius,
                        angle,
                    )
                    spread_shot.set_velocity(forward * PLAYER_SHOOT_SPEED)
                    spread_shots.append(spread_shot)
                return spread_shots

            elif self.weapon_type == "big":
                shot = BigShot(
                    self.position.x + forward.x * self.radius,
                    self.position.y + forward.y * self.radius,
                )
                shot.velocity = forward * (
                    PLAYER_SHOOT_SPEED * 0.8
                )  # Slower speed for BigShot
                return shot

        else:
            self.timer -= dt
            return None

    def update(self, dt):
        super().update(dt)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            shots = self.shoot(dt)
            if isinstance(shots, list):
                for shot in shots:
                    pass  # Add to game logic
            elif shots:
                pass  # Add to game logic

        if keys[pygame.K_q]:
            if not self.q_key_pressed:
                self.switch_weapon()
                self.q_key_pressed = True
        else:
            self.q_key_pressed = False

        self.velocity *= PLAYER_FRICTION
        self.acceleration *= PLAYER_FRICTION
