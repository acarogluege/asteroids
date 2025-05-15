import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astreoidfield import AsteroidField


def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (asteroids, updatable)


    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Screen fill color
        fill_color = (0, 0, 0)
        screen.fill(fill_color)

        # Draw the player
        for entity in drawable:
            entity.draw(screen)

        # Update the player
        updatable.update(dt)

        # Update display
        pygame.display.flip()
        dt = Clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()