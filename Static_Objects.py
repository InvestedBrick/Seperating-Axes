import pygame
from pygame import Vector2 as vec2

class Static_Object:
    def __init__(self,color):
        self.gravity = False
        self.color = color
        self.normals = []
    def render():
        pass
    def update():
        pass
    def collide():
        pass
    def calculate_normals():
        pass

class Static_Rect(Static_Object):
    def __init__(self,rect: pygame.Rect,color: tuple):
        super().__init__(color)
        self.rect = rect
        self.vertices = (rect.topleft,rect.topright,rect.bottomright,rect.bottomleft)
        self.calculate_normals()

    def render(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)
    
    
    def calculate_normals(self):
        EdgeAB = vec2(self.rect.topright[0] - self.rect.topleft[0],self.rect.topright[1] - self.rect.topleft[1])
        EdgeBC = vec2(self.rect.bottomright[0] - self.rect.topright[0],self.rect.bottomright[1] - self.rect.topright[1])
        EdgeCD = vec2(self.rect.bottomleft[0] - self.rect.bottomright[0],self.rect.bottomleft[1] - self.rect.bottomright[1])
        EdgeDA = vec2(self.rect.topleft[0] - self.rect.bottomleft[0],self.rect.topleft[1] - self.rect.bottomleft[1])

        self.normals.append(vec2(EdgeAB.y,-EdgeAB.x).normalize())
        self.normals.append(vec2(EdgeBC.y,-EdgeBC.x).normalize())
        self.normals.append(vec2(EdgeCD.y,-EdgeCD.x).normalize())
        self.normals.append(vec2(EdgeDA.y,-EdgeDA.x).normalize())


class Static_Convex_Polygon(Static_Object):
    def __init__(self,vertices : list[tuple],color: tuple):
        super().__init__(color)
        self.vertices = vertices
        self.calculate_normals()
    
    def render(self,screen):
        pygame.draw.polygon(screen,self.color,self.vertices)
    
    def calculate_normals(self):
        edges = []
        for i in range(len(self.vertices)):
            if i + 1 == len(self.vertices):
                break
            edges.append(vec2(self.vertices[i+1][0] - self.vertices[i][0],self.vertices[i+1][1] - self.vertices[i][1]))
        edges.append(vec2(self.vertices[-1][0] - self.vertices[0][0],self.vertices[-1][1] - self.vertices[0][1])) #close the polygon

        for edge in edges:
            self.normals.append(vec2(edge[1],-edge[0]).normalize())
    
