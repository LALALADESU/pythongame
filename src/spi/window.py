from typing import Union
import pygame
from .color import Color
from .image import Renderable
from .text import Text
from .shape import Point


class Window():
    def __init__(self, resolution: Point):
        self.screen: pygame.Surface = pygame.display.set_mode(resolution)
        
    def clear(self):
        self.screen.fill(Color.black())
        
    def blit(self, source: Renderable, dest: Point):
        self.screen.blit(source._get_surface(), dest, source._get_area())

    def update(self):
        pygame.display.update()
