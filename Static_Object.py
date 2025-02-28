import pygame
class Static_Object:
    def __init__(self,rect: pygame.Rect,color: tuple):
        self.rect = rect
        self.color = color
        self.gravity = False
    
    def render(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)
    
    def update(self):
        pass