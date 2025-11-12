from typing import Union
import pygame
from .color import Color
from .image import Renderable
from .text import Text
from .shape import Point


RESOLUTION = Point(640, 480)

class Window():

    _screen: pygame.Surface = pygame.display.set_mode(RESOLUTION)
    
    @classmethod
    def clear(cls):
        cls._screen.fill(Color.black())
    
    @classmethod
    def blit(cls, source: Renderable, dest: Point):
        if source is not None and dest is not None:
            cls._screen.blit(source._get_surface(), dest, source._get_area())

    @classmethod
    def update(cls):
        pygame.display.update()
