import pygame
import random

class Counter:
    def __init__(self, counter):
        self.counter = counter
        self.counter_additive = 0
        
    def increment_counter_additive(self, additive):
        self.counter_additive += additive

    def increment_counter(self, increment):
        self.counter += increment + self.counter_additive
        return self.counter

    def deincrement_counter(self, deincrement):
        self.counter -= deincrement
        return self.counter
    
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_velocity = random.uniform(-1, 1)
        self.y_velocity = random.uniform(-2, 0)
        self.lifetime = random.randint(20, 60)
        self.plus_1 = pygame.image.load('data/images/furniture/+1.png')

    def draw(self, screen):
        screen.blit(self.plus_1, (int(self.x), int(self.y)))

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
        self.lifetime -= 1

    def is_alive(self):
        return self.lifetime > 0