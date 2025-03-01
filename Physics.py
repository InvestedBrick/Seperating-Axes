from Player import *
from Static_Objects import *
from Constants import MAX_GRAVITY,GRAVITY,COLLISION_OFFSET,TYPE_RECT,TYPE_TRIANGLE
class Physics:
    def __init__(self):
        pass

    def apply_gravity(self,object):
        if object.gravity and object.vel.y < MAX_GRAVITY:
            object.vel.y += GRAVITY
    
    def handle_collisions(self,player : Player,static_objects: list[Static_Object]):
        for object in static_objects:
            if player.rect.colliderect(object.rect):
                overlap_x = min(player.rect.right - object.rect.left, object.rect.right - player.rect.left)
                overlap_y = min(player.rect.bottom - object.rect.top, object.rect.bottom - player.rect.top)

                if overlap_y < overlap_x:
                    if player.vel.y > 0:
                        player.rect.bottom = object.rect.top
                    if player.vel.y < 0:
                        player.rect.top = object.rect.bottom
                    player.vel.y = 0   
                else:
                    if player.vel.x > 0 and player.rect.x < object.rect.left:
                        player.rect.right = object.rect.left - COLLISION_OFFSET 
                    if player.vel.x < 0 and player.rect.x > object.rect.right:
                        player.rect.left = object.rect.right + COLLISION_OFFSET
                    player.vel.x = 0