import sys
import pygame
import pygame.freetype  # Import for rendering text
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    score = 0
    font = pygame.freetype.SysFont(None, 36)
    lives = 3  # Initialize lives

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updateable.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if player.collide(asteroid):
                lives -= 1
                if lives <= 0:
                    print("Game over!")
                    sys.exit(0)
                else:
                    player.position = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)  # Respawn player
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                    if asteroid.radius == ASTEROID_MAX_RADIUS:
                        score += 3  # Large asteroid
                    elif asteroid.radius == ASTEROID_MIN_RADIUS * 2:
                        score += 2  # Medium asteroid
                    elif asteroid.radius == ASTEROID_MIN_RADIUS:
                        score += 1  # Small asteroid
                    
        score_text = f"Score: {score}"
        lives_text = f"Lives: {lives}"
        font.render_to(screen, (10, 10), score_text, "white")
        font.render_to(screen, (10, 50), lives_text, "red")

        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
