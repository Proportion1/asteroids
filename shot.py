import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def rotate(self, player):
        self.rotation = player.rotation
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        
        



    def update(self, dt):
        velocity = self.velocity * dt
        self.position += velocity