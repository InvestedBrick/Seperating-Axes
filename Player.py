import pygame
from pygame import Vector2 as vec2
from Constants import MOVEMENT_SPEED
class Player:
    def __init__(self,rect: pygame.Rect,color : tuple):
        self.rect = rect
        self.color = color
        self.vel = vec2(0,0)
        self.gravity = True
        

    def render(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)    

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.vel.x = -MOVEMENT_SPEED
        elif key[pygame.K_d]:
            self.vel.x = MOVEMENT_SPEED
        else:
            self.vel.x = 0        
        

    def move(self):
        self.rect.move_ip(self.vel)
