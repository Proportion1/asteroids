import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def split(self):
        self.kill()
        
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            angle_1 = random.uniform(20, 50)
            angle_2 = random.uniform(20, 50)
            new_velocity_1 = self.velocity.rotate(angle_1)
            new_velocity_2 = self.velocity.rotate(angle_2)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = new_velocity_1 * 1.2
            asteroid_2.velocity = new_velocity_2 * 1.2
        


    def update(self, dt):
        velocity = self.velocity * dt
        self.position += velocity