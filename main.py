import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astreoidfield import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    print("Starting Asteroids!")
    
    # Get display info for better cross-device support
    display_info = pygame.display.Info()
    
    # Allow window to be resizable
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Asteroids Game")
    Clock = pygame.time.Clock()
    dt = 0
    
    # Game state variables
    score = 0
    game_time = 0
    fullscreen = False
    current_width = SCREEN_WIDTH
    current_height = SCREEN_HEIGHT
    
    # Setup font for displaying score and timer
    font = pygame.font.Font(None, 36)

    shots_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Shot.containers = (shots_group, updatable, drawable)
    player.shots_group = shots_group

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE:
                # Handle window resize
                current_width = event.w
                current_height = event.h
                screen = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    # Toggle fullscreen with F key
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        current_width, current_height = screen.get_size()
                    else:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
                        current_width = SCREEN_WIDTH
                        current_height = SCREEN_HEIGHT
            #print(list(drawable))
        
        # Update game time
        game_time += dt
               
        # Screen fill color
        fill_color = (33,86,105)
        screen.fill(fill_color)

        # Draw the player
        for entity in drawable:
            entity.draw(screen)

        # Update the player
        updatable.update(dt)
        for asteroid in asteroids:
            if hasattr(asteroid, "position") and asteroid.collision(player):
                print(f"Game Over! Final Score: {score}, Time: {int(game_time)}s")
                sys.exit()
            for shot in shots_group:
                if hasattr(shot, "position") and asteroid.collision(shot):
                    # Award points based on asteroid size
                    if asteroid.radius == ASTEROID_MIN_RADIUS:
                        score += SCORE_SMALL_ASTEROID  # Small asteroids worth more
                    elif asteroid.radius == ASTEROID_MIN_RADIUS * 2:
                        score += SCORE_MEDIUM_ASTEROID   # Medium asteroids
                    else:
                        score += SCORE_LARGE_ASTEROID   # Large asteroids
                    
                    print(f"Hit! Score: {score}")
                    shot.kill()
                    asteroid.split()
                    break
        
        # Display score and timer
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        timer_text = font.render(f"Time: {int(game_time)}s", True, (255, 255, 255))
        screen.blit(timer_text, (10, 50))
        
        # Display controls info
        small_font = pygame.font.Font(None, 24)
        controls_text = small_font.render("Controls: WASD=Move, SPACE=Shoot, F=Fullscreen", True, (200, 200, 200))
        screen.blit(controls_text, (10, current_height - 30))
        
        # Update display
        pygame.display.flip()
        dt = Clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()