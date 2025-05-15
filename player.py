from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        keys = pygame.key.get_pressed()
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, (25,51,0), self.triangle(), width=0)
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt):
        self.move(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
            
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)


        self.timer -= dt
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot(self.shots_group)
            self.timer = PLAYER_SHOOT_COOLDOWN
            

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * dt * PLAYER_SPEED
        if keys[pygame.K_s]:
            forward = pygame.Vector2(0, -1).rotate(self.rotation)
            self.position += -forward * dt * PLAYER_SPEED



    def shoot(self,shots_group):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot = Shot(self.position)
        new_shot.velocity = forward * PLAYER_SHOOT_SPEED
        shots_group.add(new_shot)