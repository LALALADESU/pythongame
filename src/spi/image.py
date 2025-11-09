import pygame
from .shape import Rectangle

class Image():
    def __init__(self, path: str, area: Rectangle = None):
        self.image = pygame.image.load(path)
        self.area = area
