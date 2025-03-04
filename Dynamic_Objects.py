import pygame
from pygame import Vector2 as vec2
from Constants import MAX_OBJ_ACC
from math import pi,cos,sin
class Dynamic_Convex_Polygon:
    def __init__(self,vertices: list[list],color: tuple,center : tuple):
        self.color = color
        self.gravity = True
        self.normals = []
        self.vertices = vertices
        self.center = center
        self.vel = vec2(0,0)
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

    def update(self):
        self.vel.x = max(-MAX_OBJ_ACC, min(self.vel.x, MAX_OBJ_ACC))
        self.vel.y = max(-MAX_OBJ_ACC, min(self.vel.y, MAX_OBJ_ACC))


    def set_ground(self,on_ground):
        self.on_ground = on_ground

    def move(self):
        self.center += self.vel
        self.rotate_vertices()
        self.vertices = [[x + self.vel.x,y + self.vel.y] for x,y in self.vertices]
        self.calculate_normals()

    def rotate_vertices(self):
        angle = self.vel.x / 10
        cos_angle = cos(angle)
        sin_angle = sin(angle)

        new_vertices = []
        for x, y in self.vertices:
            rel_x = x - self.center[0]
            rel_y = y - self.center[1]

            rotated_x = rel_x * cos_angle - rel_y * sin_angle
            rotated_y = rel_x * sin_angle + rel_y * cos_angle

            new_x = rotated_x + self.center[0]
            new_y = rotated_y + self.center[1]
            new_vertices.append([new_x, new_y])

        self.vertices = new_vertices

    