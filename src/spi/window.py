from typing import Union
import pygame
from .color import Color
from .image import Image
from .text import Text
from .shape import Point


class Window():
    def __init__(self, resolution: Point):
        self.screen: pygame.Surface = pygame.display.set_mode(resolution)
        
    def clear(self):
        self.screen.fill(Color.black())
        
    def blit(self, source: Union[Image, Text], dest: Point):
        if isinstance(source, Image):
            self.screen.blit(source.image, dest, source.area)
        if isinstance(source, Text):
            self.screen.blit(source.rendered_text, dest)
        
    def update(self):
        pygame.display.update()
