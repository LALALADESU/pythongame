import pygame


class Color(pygame.Color):
    def __init__(self, r: int, g: int, b: int, a: int = 255):
        pygame.Color.__init__(self, r, g, b, a)
    
    @staticmethod
    def black():
        return Color(0, 0, 0)
    
    @staticmethod
    def white():
        return Color(255, 255, 255)
