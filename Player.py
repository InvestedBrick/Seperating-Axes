import pygame
from pygame import Vector2 as vec2
from Constants import MOVEMENT_SPEED
class Player:
    def __init__(self,rect: pygame.Rect,color : tuple):
        self.rect = rect
        self.center = rect.center
        self.update_vertices()
        self.color = color
        self.vel = vec2(0,0)
        self.gravity = True
        self.normals = []
        self.calculate_normals()

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
        
    def set_ground(self,on_ground):
        self.on_ground = on_ground

    def move(self):
        self.rect.move_ip(self.vel)
        self.update_vertices()
        self.calculate_normals()

    def update_vertices(self):
        self.vertices = (self.rect.topleft,self.rect.topright,self.rect.bottomright,self.rect.bottomleft)

    
    def calculate_normals(self):
        self.normals.clear()
        EdgeAB  = vec2(self.rect.topright[0] - self.rect.topleft[0],self.rect.topright[1] - self.rect.topleft[1])
        EdgeBC  = vec2(self.rect.bottomright[0] - self.rect.topright[0],self.rect.bottomright[1] - self.rect.topright[1])
        EdgeCD  = vec2(self.rect.bottomleft[0] - self.rect.bottomright[0],self.rect.bottomleft[1] - self.rect.bottomright[1])
        EdgeDA  = vec2(self.rect.topleft[0] - self.rect.bottomleft[0],self.rect.topleft[1] - self.rect.bottomleft[1])

        self.normals.append(vec2(EdgeAB[1],-EdgeAB[0]).normalize())
        self.normals.append(vec2(EdgeBC[1],-EdgeBC[0]).normalize())
        self.normals.append(vec2(EdgeCD[1],-EdgeCD[0]).normalize())
        self.normals.append(vec2(EdgeDA[1],-EdgeDA[0]).normalize())
