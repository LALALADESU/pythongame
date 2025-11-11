import pygame
from .color import Color
from .image import Renderable


class Font():
    def __init__(self, path: str):
        self.path = path


class Text(Renderable):
    def __init__(
        self, text: str, font: Font = Font(None), size: int = 16, color: Color = Color.white(),
        bgcolor: Color = None, antialias: bool = False, bold: bool = False, italic: bool = False,
        underline: bool = False, strikethrough: bool = False
    ):
        self.font = font if font is not None else Font(None)
        self.size = size
        self.text = text
        
        self.color = color
        self.bgcolor = bgcolor
        self.antialias = antialias
        
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.strikethrough = strikethrough
        
        self.pygame_font: pygame.font.Font
        self.rendered_text: pygame.Surface
        
        self._reload_font()
        self._rerender_text()
        
    def _reload_font(self):
        self.pygame_font = pygame.font.Font(self.font.path, self.size)
        self.pygame_font.set_bold(self.bold)
        self.pygame_font.set_italic(self.italic)
        self.pygame_font.set_underline(self.underline)
        self.pygame_font.set_strikethrough(self.strikethrough)
    
    def _rerender_text(self):
        color = pygame.Color(self.color.r, self.color.g, self.color.b, self.color.a)
        bgcolor = pygame.Color(self.bgcolor.r, self.bgcolor.g, self.bgcolor.b, self.bgcolor.a) if self.bgcolor is not None else None
        self.rendered_text = self.pygame_font.render(self.text, self.antialias, color, bgcolor)
        
    def _get_surface(self):
        return self.rendered_text
    
    def _get_area(self):
        return None
        
    def set_font_path(self, font: Font):
        self.font = font
        self._reload_font()
        self._rerender_text()
        
    def set_size(self, size: int):
        self.size = size
        self._reload_font()
        self._rerender_text()
        
    def set_text(self, text: str):
        self.text = text
        self._rerender_text()
    
    def set_antialias(self, antialias: bool):
        self.antialias = antialias
        self._rerender_text()
        
    def set_color(self, color: Color):
        self.color = color
        self._rerender_text()
        
    def set_bgcolor(self, bgcolor: Color):
        self.bgcolor = bgcolor
        self._rerender_text()
        
    def set_bold(self, bold: bool):
        self.bold = bold
        self.pygame_font.set_bold(bold)
        self._rerender_text()
        
    def set_italic(self, italic: bool):
        self.italic = italic
        self.pygame_font.set_italic(italic)
        self._rerender_text()
        
    def set_underline(self, underline: bool):
        self.underline = underline
        self.pygame_font.set_underline(underline)
        self._rerender_text()
    
    def set_strikethrough(self, strikethrough: bool):
        self.strikethrough = strikethrough
        self.pygame_font.set_strikethrough(strikethrough)
        self._rerender_text()
