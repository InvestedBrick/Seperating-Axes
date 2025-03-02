from Player import *
from Static_Objects import *
from Constants import MAX_GRAVITY,GRAVITY
class Physics:
    def __init__(self):
        pass

    def apply_gravity(self,object):
        if object.gravity and object.vel.y < MAX_GRAVITY: #and not object.on_ground:
            object.vel.y += GRAVITY
    #maybe I should do an own SAT class
    def handle_collisions(self,player : Player,static_objects: list[Static_Object]):
        overlap = float('inf')
        smallest = vec2(0,0)
        total = vec2(0,0)
        break_continue = False
        player.set_ground(False)
        for object in static_objects:
            for axis in object.normals:
                prj1 = self.get_projection(object,axis)
                prj2 = self.get_projection(player,axis)
                if  self.are_overlapping(prj1,prj2):
                    o = self.get_overlap(prj1,prj2)
                    if (o < overlap):
                       overlap = o
                       smallest = axis
                else:
                    break_continue = True
                    break
            if break_continue:
                break_continue = False
                continue
            for axis in player.normals:
                prj1 = self.get_projection(object,axis)
                prj2 = self.get_projection(player,axis)
                if not self.are_overlapping(prj1,prj2):
                    break_continue = True
                    break
                else:
                    o = self.get_overlap(prj1,prj2)
                    if (o < overlap):
                       overlap = o
                       smallest = axis
                   
            if break_continue:
                break_continue = False
                continue

            closest_point = self.get_closest_point(player, object)
            direction = vec2(player.rect.x,player.rect.y) - closest_point
            
            if smallest.dot(direction) < 0:
                smallest = -smallest

            if abs(smallest.x) > abs(total.x):
                total.x = smallest.x
            if abs(smallest.y) > abs(total.y):
                total.y = smallest.y

        player.vel += total
        if total.y < 0:
            player.vel.y = -1
            player.set_ground(True)
        

    def get_closest_point(self,player, object):
        closest_point = vec2(0,0)
        closest_dist = float('inf')

        for point in object.vertices:
            dist = vec2(vec2(player.rect.x,player.rect.y) - point).magnitude()
            if dist < closest_dist:
                closest_dist = dist
                closest_point = point

        return closest_point
    
    def are_overlapping(self,prj1,prj2):
        return not (prj1[1] < prj2[0] or prj2[1] < prj1[0])

    def get_overlap(self, prj1, prj2):
        return min(prj1[1], prj2[1]) - max(prj1[0], prj2[0])

    def get_projection(self,shape,axis):
        min = axis[0] * shape.vertices[0][0] + axis[1] * shape.vertices[0][1]
        max = min

        for vertex in shape.vertices:
            p = axis[0] * vertex[0] + axis[1] * vertex[1]
            if p < min:
                min = p
            elif p > max:
                max = p
        
        return (min,max)