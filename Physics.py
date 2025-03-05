from Player import *
from Static_Objects import *
from Constants import MAX_GRAVITY, GRAVITY
from Dynamic_Objects import Dynamic_Convex_Polygon
class Physics:
    def __init__(self):
        pass

    def apply_gravity(self, obj):
        if obj.gravity and obj.vel.y < MAX_GRAVITY:
            obj.vel.y += GRAVITY

    def handle_collisions(self, dynamic_object:   Dynamic_Convex_Polygon, objects: list[Static_Object]):
        max_iterations = 2  # Prevents potential infinite loops
        iteration = 0
        downwards_collision = False
        dynamic_object.set_ground(False)    
        while iteration < max_iterations:
            collision_found = False
            for obj in objects:
                # dont collide with yourself
                if obj == dynamic_object:
                    continue
                mtv = self.get_collision_mtv(dynamic_object, obj)
                if mtv is not None:
                    if mtv.y < 0:
                        downwards_collision = True
                    dynamic_object.vel += mtv / 2
                    collision_found = True
            if not collision_found:
                break  
            iteration += 1
        
        if dynamic_object.vel.y < 0 and downwards_collision:
            dynamic_object.vel.y = -1
            dynamic_object.set_ground(True)
    
    def get_collision_mtv(self, player : Dynamic_Convex_Polygon, static_object : Static_Convex_Polygon):
        """
        Computes the Minimum Translation Vector (MTV) that would resolve the collision
        between player and static_object using the Separating Axis Theorem.
        Returns None if there is no collision.
        """
        mtv_overlap = float('inf')
        mtv_axis = None
        
        axes = static_object.normals + player.normals
        
        for axis in axes:
            prj_obj = self.get_projection(static_object, axis)
            prj_player = self.get_projection(player, axis)
            
            if not self.are_overlapping(prj_obj, prj_player):
                return None
            else:
                overlap = self.get_overlap(prj_obj, prj_player)
                if overlap < mtv_overlap:
                    mtv_overlap = overlap
                    mtv_axis = axis
        
        if mtv_axis is None:
            return None
        
        closest_point = self.get_closest_point(player, static_object)
        direction = vec2(player.center) - closest_point
        if mtv_axis.dot(direction) < 0:
            mtv_axis = -mtv_axis
        
        return mtv_axis * mtv_overlap

    def get_closest_point(self, player, static_object: Static_Convex_Polygon):
        closest_point = vec2(0, 0)
        closest_dist = float('inf')
        for point in static_object.vertices:
            dist = (vec2(player.center) - point).magnitude()
            if dist < closest_dist:
                closest_dist = dist
                closest_point = point
        return closest_point

    def are_overlapping(self, prj1, prj2):
        return not (prj1[1] < prj2[0] or prj2[1] < prj1[0])

    def get_overlap(self, prj1, prj2):
        return min(prj1[1], prj2[1]) - max(prj1[0], prj2[0])

    def get_projection(self, shape, axis):
        min_proj = axis[0] * shape.vertices[0][0] + axis[1] * shape.vertices[0][1]
        max_proj = min_proj
        for vertex in shape.vertices:
            proj = axis[0] * vertex[0] + axis[1] * vertex[1]
            if proj < min_proj:
                min_proj = proj
            elif proj > max_proj:
                max_proj = proj
        return (min_proj, max_proj)
