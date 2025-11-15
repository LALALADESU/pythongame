import pygame
from .shape import Point, Rectangle
from .time import Time, TimeUnit
from functools import lru_cache
from typing import Union


class Renderable():
    def _get_surface(self) -> pygame.Surface: ...
    def _get_area(self)    -> Union[Rectangle, None]: ...
    def _get_offset(self)  -> Union[Point, None]: ...


class Image(Renderable):
    def __init__(self, path: str, area: Union[Rectangle, None] = None, offset: Union[Point, None] = None):
        """
        `path` : image file path
        `area` : sub area of a image (None: whole image)
        `offset` : render offset (anchor: topleft) (None: no offset)
        """
        self.path   = path
        self.image  = self._load_image(path)
        self.area   = area
        self.offset = offset

    @staticmethod
    @lru_cache()
    def _load_image(path):
        return pygame.image.load(path)

    # Renderable
    def _get_surface(self): return self.image
    def _get_area(self):    return self.area
    def _get_offset(self):  return self.offset


class Animation(Renderable):
    def __init__(self, images: list[Image], durations: list[float], is_loop: bool = False):
        """
        `images` : frames to render
        `durations` : durations of each frame (unit: second)
        `is_loop` : whether loop the animation
        """
        self.is_playing = False
        self.is_loop = is_loop
        self.timer: float = 0
        self.index = 0
        
        self.images = images
        self.durations = durations


    def update(self):
        if not self.is_playing: return
        
        self.timer += Time.get_timedelta()
        if self.timer >= self.durations[self.index]:
            self.timer = 0
            
            if self.index < len(self.images) - 1:
                self.index += 1
            else:
                if self.is_loop:
                    self.index = 0
                else:
                    self.is_playing = False

          
    def start(self):
        self.is_playing = True
        
    def pause(self):
        self.is_playing = False
        
    def stop(self):
        self.is_playing = False
        self.timer = 0
        self.index = 0
        
    def get_is_playing(self):
        return self.is_playing
    
    def get_timer(self):
        return self.timer
    
    def set_timer(self, timer: float):
        self.timer = timer
        
    def get_index(self):
        return self.index
    
    def set_index(self, index: int):
        if   index < 0: self.index = 0
        elif index > len(self.images): self.index = len(self.images) - 1
        else: self.index = index
    
    def _get_surface(self): return self.images[self.index]._get_surface()
    def _get_area(self):    return self.images[self.index]._get_area()
    def _get_offset(self):  return self.images[self.index]._get_offset()
    