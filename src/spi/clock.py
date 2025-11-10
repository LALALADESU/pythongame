import pygame
import time


class Clock():
    def __init__(self):
        self._clock = pygame.time.Clock()
    
    def tick(self, fps: float):
        self._clock.tick(fps)
    
    def get_fps(self):
        return self._clock.get_fps()