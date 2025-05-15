from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        


    def draw(self, surface):
        pygame.draw.circle(surface, (0,0,0), (int(self.position.x), int(self.position.y)), self.radius, width=0)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        self.x = self.position.x
        self.y = self.position.y
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2