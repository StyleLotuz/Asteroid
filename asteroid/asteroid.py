from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(angle)
        vector_two = self.velocity.rotate(-angle)
        new_asteroid_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid_one.velocity = vector_one * 1.2
        new_asteroid_two.velocity = vector_two * 1.2

        
        

