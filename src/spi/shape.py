import pygame


class Shape():
    def __init__(self):
        self.x: float
        self.y: float
        
    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
    

class Point(Shape, pygame.Vector2):
    def __init__(self, x: float, y: float):
        pygame.Vector2.__init__(self, x, y)
    
    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"


class Line(Shape):
    """Line Segment"""
    def __init__(self, x: float, y: float, x2: float, y2: float):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
    
    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, x2={self.x2}, y2={self.y2})"


class Rectangle(Shape, pygame.Rect):
    def __init__(self, x: float, y: float, w: float, h: float):
        pygame.Rect.__init__(self, (x, y, w, h))
    
    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, w={self.w}, h={self.h})"


class Circle(Shape):
    def __init__(self, x: float, y: float, r: float):
        self.x = x
        self.y = y
        self.r = r
    
    def __str__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, r={self.r})"
