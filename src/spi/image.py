import pygame
from .shape import Rectangle
from .time import Time, TimeUnit
from functools import lru_cache


class Renderable():
    def _get_surface(self) -> pygame.Surface: ...
    def _get_area(self) -> Rectangle: ...


class Image(Renderable):
    def __init__(self, path: str, area: Rectangle = None):
        self.image = self._load_image(path)
        self.area = area

    def _get_surface(self):
        return self.image
    
    def _get_area(self):
        return self.area
    
    @staticmethod
    @lru_cache()
    def _load_image(path):
        return pygame.image.load(path)


class Animation(Renderable):
    def __init__(self, images: list[Image], durations: list[float], timeunit: TimeUnit = TimeUnit.SECOND, is_loop: bool = False):
        self.is_playing = False
        self.is_loop = is_loop
        self.timer: float = 0
        self.index = 0
        
        self.images = images
        self.durations = [TimeUnit.convert(x, timeunit, TimeUnit.SECOND) for x in durations]


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
    
    def _get_surface(self):
        return self.images[self.index]._get_surface()
    
    def _get_area(self):
        return self.images[self.index]._get_area()
    