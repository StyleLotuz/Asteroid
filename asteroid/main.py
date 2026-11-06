import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (drawable, updatable, shots)

    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        for thing in asteroids:
            if thing.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for thing in asteroids:
            for shoot in shots:
                if shoot.collides_with(thing):
                    log_event("asteroid_shot")
                    thing.split()
                    shoot.kill()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
