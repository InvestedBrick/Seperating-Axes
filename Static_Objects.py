import pygame
from Constants import TYPE_RECT,TYPE_TRIANGLE
# Completely overwork this stuff, implement SAT collision
class Static_Object:
    def __init__(self):
        self.gravity = False

    def render():
        pass
    def update():
        pass

class Static_Rect(Static_Object):
    def __init__(self,rect: pygame.Rect,color: tuple):
        super().__init__()
        self.rect = rect
        self.color = color
        self.type = TYPE_RECT
    
    def render(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)
    

class Static_Triangle(Static_Object):
    def __init__(self,points : list[tuple],color: tuple):
        super().__init__()
        self.points = points
        self.color = color
        self.type = TYPE_TRIANGLE
    
    def render(self,screen):
        pygame.draw.polygon(screen,self.color,self.points)
    
